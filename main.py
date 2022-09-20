from pyspark import SparkConf, SparkContext
from pyspark.mllib.recommendation import MatrixFactorizationModel
from pyspark.mllib.recommendation import ALS


def create_spark_context():
    global sc, path
    sc = SparkContext(conf=SparkConf().setAppName('test'))
    path = "hdfs://node1:8020/input/"


def save_model():
    rdd = sc.textFile(path + "u.data")
    rawRatings = rdd.map(lambda x: x.split('\t')[0:3])
    ratingRDD = rawRatings.map(lambda x: (x[0], x[1], x[2]))
    model = ALS.train(ratingRDD, 10, 8, 0.01)
    model.save(sc, path+"ALSmodel/")
    print("Save the model successful!")


def prepare_data():
    print("Begin to read the movie id and name as a dictionary...")
    itemRDD = sc.textFile(path + "u.item")
    dict_movie_title = itemRDD.map(lambda line: line.split("|")) \
        .map(lambda a: (float(a[0]), a[1])) \
        .collectAsMap()
    return dict_movie_title


def recommend_movies(model, movie_title, input_user_id):
    recommend_movie = model.recommendProducts(input_user_id, 10)
    print("To user_id" + str(input_user_id) + "Recommend these movies:")
    for rmd in recommend_movie:
        print("To user id {0}, recommend the movie {1}. The score is {2}".format(rmd[0], movie_title[rmd[1]], rmd[2]))


def recommend_users(model, movie_title, input_movie_id):
    recommend_user = model.recommendUsers(input_movie_id, 10)
    print("To movie id {0}, movie name is :{1}. Recommend these users id:".format(input_movie_id, movie_title[input_movie_id]))
    for rmd in recommend_user:
        print("To user_id {0} , The score is {1}".format(rmd[0], rmd[2]))


def load_model():
    try:
        sc.textFile(path + "ALSmodel/metadata").collect()
    except Exception:
        print("Can't find the ALSModel model, need to train one")
        save_model()
    print("Load the ALSModel model.")
    model = MatrixFactorizationModel.load(sc, path + "ALSmodel/")
    return model


def recommend(model, id, type):
    if type == "-u":
        recommend_movies(model, movieTitle, int(id))
    if type == "-m":
        recommend_users(model, movieTitle, int(id))


if __name__ == "__main__":
    create_spark_context()
    print("==========Read data===============")
    movieTitle = prepare_data()
    print("==========Load model===============")
    my_model = load_model()
    print("==========Recommend===============")
    # my_id = input("Please input the id:")  # such as 100
    # my_type = input("Please input the type:")  # such as -u
    recommend(my_model, 100, '-u')
