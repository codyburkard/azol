"""A module containing a client for interacting with the Kudu API.
"""
import logging

from azol.clients.oauth_http_client import OAuthHTTPClient
from azol.constants import OAuthResourceIDs
from html.parser import HTMLParser

class SCMEnvVarHTMLParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self._env_variables = {}
        self.new_data=''

    def get_env_variables(self):
        return self._env_variables

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self.new_data=''

    def handle_endtag(self, tag):
        if tag == "li":
            key, val = self.new_data.split( " = " )
            self._env_variables[key] = val
            self.new_data=''

    def handle_data(self, data):
        self.new_data = data

class ScmRequestFailedException(Exception):
    """
        Exception that is raised when requests to SCM
        unexpectedly fail
    """

class KuduClient( OAuthHTTPClient ):
    """
        An HTTP client for interacting with the App Service Kudu resource
    """
    
    def __init__( self, scm_url, *args, **kwargs ):
        super().__init__( oauth_resource=OAuthResourceIDs.Arm, base_url=scm_url, *args, **kwargs)

    def get_env_variables(self):

        response = self._send_request( f"/Env", method="GET" )
        if response.status_code != 200:
            logging.error( "%s error on SCM API request to get environment variables"
                        "Raw error: %s", response.status_code,
                        response.content )
            raise ScmRequestFailedException()
        
        # Get the index of the beginning of the environment variables in HTML
        content = str(response.content)
        start_index_value = "<h3 id=\"envVariables\">Environment variables</h3>"
        start_index = content.index(start_index_value) + len(start_index_value)
        end_index_value = "<h3 id=\"path\">PATH</h3>"
        end_index = content.index(end_index_value)

        env_variable_html_content=content[start_index:end_index]

        parser = SCMEnvVarHTMLParser()
        parser.feed(env_variable_html_content)

        return parser.get_env_variables()

    def get_processes(self):

        response = self._send_request( f"/api/processes",
                                    method="GET" )
        if response.status_code != 200:
            logging.error( "%s error on SCM API request to get processes"
                        "Raw error: %s", response.status_code,
                        response.content )
            raise ScmRequestFailedException()
        return response.json()

    def get_process(self, pid):

        response = self._send_request( f"/api/processes/{pid}",
                                    method="GET" )
        if response.status_code != 200:
            logging.error( "%s error on SCM API request to get process"
                        "Raw error: %s", response.status_code,
                        response.content )
            raise ScmRequestFailedException()
        return response.json()

    def get_process_dump(self, pid):

        response = self._send_request( f"/api/processes/{pid}/dump",
                                    method="GET" )
        if response.status_code != 200:
            logging.error( "%s error on SCM API request to get process dump"
                        "Raw error: %s", response.status_code,
                        response.content )
            raise ScmRequestFailedException()
        return response.content

    def ls(self, path):
        response = self._send_request( f"/api/vfs/{path}",
                                    method="GET" )
        if response.status_code != 200:
            logging.error( "%s error on SCM API request to list directory contents"
                        "Raw error: %s", response.status_code,
                        response.content )
            raise ScmRequestFailedException()
        return response.json()

    def get_file(self, path):
        response = self._send_request( f"/api/vfs/{path}",
                                    method="GET" )
        if response.status_code != 200:
            logging.error( "%s error on SCM API request to get file"
                        "Raw error: %s", response.status_code,
                        response.content )
            raise ScmRequestFailedException()
        return response.content

    def command( self, command, directory=None ):
        """Execute a command via the Kudu API.
        
        Returns:
            A dict containing the results of the command

        """
        body={
            "command":command
        }
        if directory is not None:
            body["dir"]=directory
        raw_response = self.post( "/api/command", json=body )

        if raw_response.status_code != 200:
            logging.error( "ERROR while running command via kudu: %s", raw_response.content )
            raise Exception()
        res = raw_response.json()

        return res
    
    def get_settings( self ):
        """Get settings
        
        Returns:
            A dict containing the settings

        """
        
        raw_response = self.get( "/api/settings" )

        if raw_response.status_code != 200:
            logging.error( "ERROR while running command via kudu: %s", raw_response.content )
            raise Exception()
        res = raw_response.json()

        return res
    
    def get_setting( self, setting ):
        """Get setting
        
        Returns:
            A dict containing the settings

        """
        
        raw_response = self.get( f"/api/settings/{setting}" )

        if raw_response.status_code != 200:
            logging.error( "ERROR while running command via kudu: %s", raw_response.content )
            raise Exception()
        res = raw_response.content

        return res

      