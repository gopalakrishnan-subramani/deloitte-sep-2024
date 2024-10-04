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


