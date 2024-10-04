# KAFKA Window SETUP
 
```
https://kafka.apache.org/downloads

https://downloads.apache.org/kafka/3.8.0/kafka_2.12-3.8.0.tgz

Extract kafka_2.12-3.8.0.tgz files
```

```
Copy the extracted folder that contains files to C:\kafka_2.12-3.8.0

Open command prompt


Windows start => env => edit system environemnt variabeles enter

You can either add to system [might need admin] or user environment [no admin]
choose user environment
```

```
not a command
Ensure env KAFKA_HOME set to C:\kafka_2.12-3.8.0
```


open command prompt
```
cd %KAFKA_HOME%


%KAFKA_HOME%\bin\windows\zookeeper-server-start.bat %KAFKA_HOME%\config\zookeeper.properties
```

Open second command prompt
```
cd %KAFKA_HOME%

%KAFKA_HOME%\bin\windows\kafka-server-start.bat %KAFKA_HOME%\config\server.properties
```

## KAFKA EXAMPLE COMMANDS 

create topic
```
%KAFKA_HOME%\bin\windows\kafka-topics  --create --topic quickstart-events --bootstrap-server localhost:9092
```

list topic

```
%KAFKA_HOME%\bin\windows\kafka-topics --list   --bootstrap-server localhost:9092
```


describe topic

```
%KAFKA_HOME%\bin\windows\kafka-topics --describe --topic quickstart-events --bootstrap-server localhost:9092
```

Start a producer to send records

start new command line on cmd, you will see a prompt >  there you could text and hit ENTER

```
%KAFKA_HOME%\bin\windows/kafka-console-producer --topic quickstart-events --bootstrap-server localhost:9092
```


start a console consumer on new cmd

start new command prompt


```
%KAFKA_HOME%\bin\windows/kafka-console-consumer --topic quickstart-events --bootstrap-server localhost:9092
```


Now type some text on producer window, hit ENTER key and see the consumer window for susbcribe


# Local Jupyter lab without cluster

```

conda create bigdata python=3.10

pip3 install --upgrade pip

pip install jupyterlab

pip install pyspark
pip install findspark

```

Every day

start button, type mini conda, launch cmd on mini conda
```



(base) c:\users\yourname> conda activate bigdata

(bigdata) c:\users\yourname> jupyter lab


 
```

# Hadoop Winutils for Windows

Hadoop deployment made for linux, few commands not supported by windows

Free drivers for Windows avaiable

https://github.com/steveloughran/winutils



Download zip file

Extract the downloaded zip file

Copy the folder hadoop-3.0.0 to c:\hadoop-3.0.0

'''
Set Envrionment variable 

start menu -> type env -> run environment variable., add to user variable

HADOOP_HOME c:\hadoop-3.0.0 on Windows

ADD c:\hadoop-3.0.0\bin to Windows PATH environment Variable
'''

# Setup Local Spark Development


https://spark.apache.org/downloads.html

download and extract the zip file   https://www.apache.org/dyn/closer.lua/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz

Extract spark-3.5.3-bin-hadoop3.tgz

copy the extracted subfolder  spark-3.5.3-bin-hadoop3   into c:\spark-3.5.3-bin-hadoop3  

ensure that the folder you copy has all files


Set the envrionment path

Start -> search env -> launch envrionment variebles (user variables)

add SPARK_HOME with path c:\spark-3.5.3-bin-hadoop3


# START SPARK CLUSTER

Command you may need to change based on ip address or use localhost

We start master with two workers, in production, the workers shall be from different machines.. 

Start master

```
cd %SPARK_HOME%

bin\spark-class org.apache.spark.deploy.master.Master
```

This start spark master  spark://192.168.0.199:7077, your ip it binds to, copy the master url, use in below command

Spark UI /DAG/Stages/etc start at port http://localhost:8080 

start worker 1
```
cd %SPARK_HOME%
bin\spark-class org.apache.spark.deploy.worker.Worker spark://192.168.0.199:7077
```

start worker 2
```
cd %SPARK_HOME%
bin\spark-class org.apache.spark.deploy.worker.Worker spark://192.168.0.199:7077
```




