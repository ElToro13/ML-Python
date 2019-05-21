import got3
import pandas as pd
from time_keeper import count
from multiprocessing import Pool
import numpy as np

def get_tweets(phrase):
    data=[]
    tweetCriteria = got3.manager.TweetCriteria().setQuerySearch(phrase).setSince("2018-01-01").setUntil("2018-12-31").setMaxTweets(0)
    print(len(got3.manager.TweetManager.getTweets(tweetCriteria)))
    for i in range(0, len(got3.manager.TweetManager.getTweets(tweetCriteria))):
        try:
            print(i)
            tweet = got3.manager.TweetManager.getTweets(tweetCriteria)[i]
            date, time = str(tweet.date).split(" ")
            data.append([tweet.text, time, date, tweet.username])
        except Exception as e:
            print("Error in {} because of {}".format(str(i), e))
    
    dat = np.array(data)
    df = pd.DataFrame(data=dat)
    df.to_csv("{}_Final.csv".format(phrase), header=False, index=False)

"""
Here, I have divided the whole process into 3 parallel pipelines. The tags "Elderly fell down", "grandma tripped", "elderly got hurt" will be searched for with this API
simultaneously. Thus, getting results quicker and saving time. The line "pool = Pool(processes=3)" decides the number of parallel process that python will run.
Note: My laptop supports 12 multithreading(6 cores i.e. per core 2 threads so 6 X 2 = 12 threads). Thus the safe values for my laptop would be 8 or 9 as other process also goes on windows. 
"""
if __name__ == "__main__":
    cnt = count()
    cnt.start()
    #pool = Pool(processes=1)
    print("Starting..")
    #pool.map(get_tweets, ["Elderly fell down"])#, "grandma tripped", "elderly got hurt"])
    get_tweets("grandma tripped")
    stats = cnt.finish()
    print("Time Elasped: {} mins : {} secs".format(stats["mins"], stats["secs"]))


