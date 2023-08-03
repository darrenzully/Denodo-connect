from socket import gethostname

import jaydebeapi as dbdriver
import jpype


# Constants for SSL options
QUERY_TIMEOUT = 3000
SSL_ENABLED = True

def connect(hostname: str, port: str, vdbname: str, usr: str, pss: str, driver_path: str, user_agent: str = None):
    if not user_agent:
        client_hostname = gethostname()
        user_agent = f"{dbdriver.__name__}-{client_hostname}"

    conn_uri = f"jdbc:vdb://{hostname}:{port}/{vdbname}?ssl={SSL_ENABLED}&queryTimeout={QUERY_TIMEOUT}&userAgent={user_agent}"
    user = usr
    passwd = pss

    return dbdriver.connect("com.denodo.vdp.jdbc.Driver",
                            conn_uri,
                            driver_args={"user": user,
                                         "password": passwd},
                            jars=driver_path)

def check_and_connect(hostname: str, port: str, vdbname: str, usr: str, pss: str, driver_path: str, trust_path: str, user_agent: str = None):
    if not user_agent:
        client_hostname = gethostname()
        user_agent = f"{dbdriver.__name__}-{client_hostname}"

    conn_uri = f"jdbc:vdb://{hostname}:{port}/{vdbname}?ssl={SSL_ENABLED}&queryTimeout={QUERY_TIMEOUT}&userAgent={user_agent}"

    user = usr
    passwd = pss

    if not jpype.isJVMStarted():
        jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=" + driver_path, "-Djavax.net.ssl.trustStore=" + trust_path)

    return dbdriver.connect("com.denodo.vdp.jdbc.Driver",
                            conn_uri,
                            driver_args={"user": user,
                                         "password": passwd},
                            jars=driver_path)
