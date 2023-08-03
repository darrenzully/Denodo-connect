import jaydebeapi as dbdriver
import jpype

USERAGENT = "denodo-connect"

def connect(hostname: str, port: str, vdbname: str, usr: str, pss: str, driver_path: str):
    conn_uri = f"jdbc:vdb://{hostname}:{port}/{vdbname}?ssl=true&queryTimeout=3000&userAgent={USERAGENT}"
    user = usr
    passwd = pss
 
    conn = dbdriver.connect( "com.denodo.vdp.jdbc.Driver",
                            conn_uri,
                            driver_args = {"user": user,
                                            "password": passwd},
                            jars = driver_path
                            )
    return conn

def check_and_connect(hostname: str, port: str, vdbname: str, usr: str, pss: str, driver_path: str, trust_path: str):
    
    conn_uri = f"jdbc:vdb://{hostname}:{port}/{vdbname}?ssl=true&queryTimeout=3000&userAgent={USERAGENT}"
   
    user = usr
    passwd = pss
 
    if (not jpype.isJVMStarted()):
        jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=" + driver_path,
            "-Djavax.net.ssl.trustStore=" + trust_path)
 
    conn = dbdriver.connect( "com.denodo.vdp.jdbc.Driver",
                            conn_uri,
                            driver_args = {"user": user,
                                            "password": passwd},
                            jars = driver_path
                            )
    return conn