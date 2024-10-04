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
