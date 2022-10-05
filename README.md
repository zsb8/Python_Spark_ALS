This is a sample code. Data is pubic.
# Python_Spark_ALS
Use ALS on Spark to create a recommend engine.      

# Run the code
Type this command on Linux, use **spark-submit** to run the code.
## Get most favourite movies for one user
You input a user id such as 100, then input the type as -u, then the engine will push the most favourite movies to this id=100 user.  
```
spark-submit --master spark://node1:7077  /tmp/pycharm_project_485/01_RDD/test.py
```
Got the result:    
![image](https://user-images.githubusercontent.com/75282285/191274710-c444c420-4071-4024-9ff4-a8832c7371f7.png)

## Get people who most likely to wath the movie
You input a moive id such as 200, then input the type as -m, then the engine will recommend people who most likely to wath the id=200 movie.  
```
spark-submit --master spark://node1:7077  /tmp/pycharm_project_485/01_RDD/test.py
```
![image](https://user-images.githubusercontent.com/75282285/191279163-943e79f6-91b2-437c-853d-9c805df8237d.png)


# Spark Master
You can find the Running Applications on [Spark](http://node1:8080/)     
![image](https://user-images.githubusercontent.com/75282285/191274075-83e1e385-da5b-40b2-b837-5c7579ca71d0.png)

You can see it used 3 machine to currency calculate. 
![image](https://user-images.githubusercontent.com/75282285/191274515-515cc48c-4a36-462b-8df0-fdc8c4df3629.png)

# Spark History Server
You can access [the history page](http://node1:18080/) to view the history tasks.
![image](https://user-images.githubusercontent.com/75282285/191275669-86006980-cc76-4723-8d07-04ff7e7398b0.png)

You can see one application's Spark Jobs. It used 3 `executors` to work.
![image](https://user-images.githubusercontent.com/75282285/191275856-9ce4ef9f-affe-4e78-b408-0a340797350e.png)

You can see the *DAG Visualization* of one job in the task.
![image](https://user-images.githubusercontent.com/75282285/191276558-961f3e7f-587e-4b1a-be57-7ac46eb249f4.png)

# Services
ResourceManager    
![image](https://user-images.githubusercontent.com/75282285/191279864-019d9b57-6ebc-4634-aecc-3c64d3e75a64.png)

NodeManager    
![image](https://user-images.githubusercontent.com/75282285/191279701-b9a4de9d-04fc-41dd-8104-319cd804dce6.png)

