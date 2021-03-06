import os
import psutil

# support local python script developmnet
in_colab=True
try:
    from google.colab.output import eval_js
    spark_home='/content/spark-3.0.2-bin-hadoop3.2'
except:
    in_colab=False
    spark_home='spark-3.0.2-bin-hadoop3.2'

def install_all():

    print("installing spark and starting proxy")

    if in_colab:
        rurl=eval_js("google.colab.kernel.proxyPort(9090)")
        print("url for Spark UI")
        print(rurl)
        os.system("apt-get install openjdk-8-jdk-headless -qq > /dev/null")
        os.system("update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java")

    if not(os.path.exists(spark_home)):
        os.system('wget -q https://downloads.apache.org/spark/spark-3.0.2/spark-3.0.2-bin-hadoop3.2.tgz')
        os.system('tar xf spark-3.0.2-bin-hadoop3.2.tgz')
        os.system('rm spark-3.0.2-bin-hadoop3.2.tgz')

    #os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
    os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
    os.environ["SPARK_HOME"] = spark_home
    os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"

    start_proxy=True
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            cmdLine = proc.cmdline()
            processID = proc.pid
            try:
                if 'ui_proxy.py' in cmdLine[1]:
                    print(cmdLine , ' ::: ', processID)
                    start_proxy=False
                    break
            except:
                pass
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if start_proxy:
        cmd = "nohup python3 {}/ui_proxy.py &".format(os.path.dirname(__file__))
        print(cmd)
        os.system(cmd)
