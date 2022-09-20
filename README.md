# Python_Spark_ALS
Use ALS on Spark to create a recommend engine

# Run the code
Type this command on Linux, use spark-submit to run the code.
```
spark-submit --master spark://node1:7077  /tmp/pycharm_project_485/01_RDD/test.py
```
Got the result:    
![image](https://user-images.githubusercontent.com/75282285/191274710-c444c420-4071-4024-9ff4-a8832c7371f7.png)

# Spark Master
You can find the Running Applications on Spark http://node1:8080/     
![image](https://user-images.githubusercontent.com/75282285/191274075-83e1e385-da5b-40b2-b837-5c7579ca71d0.png)

You can see it used 3 machine to currency calculate. 
![image](https://user-images.githubusercontent.com/75282285/191274515-515cc48c-4a36-462b-8df0-fdc8c4df3629.png)

# Spark History Server
You can access http://node1:18080/ to view the history tasks.
![image](https://user-images.githubusercontent.com/75282285/191275669-86006980-cc76-4723-8d07-04ff7e7398b0.png)

You can see one application's Spark Jobs. It used 3 nodes to work together.
![image](https://user-images.githubusercontent.com/75282285/191275856-9ce4ef9f-affe-4e78-b408-0a340797350e.png)

