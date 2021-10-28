import pandas as pd
import matplotlib.pyplot as plt

if __name__=="__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_rows', None)
    for sf in (7, 12):
        for dbm in (3, 14):
            for bw in (125,250):
                df15 = pd.read_csv('J:/Atieh/University/Internet of things/homeworks/hw3/results/res-15-'+str(sf)+'-'
                                   +str(dbm)+'-'+str(bw)+'.csv')
                totalReceivedPackets15 = 0
                sentPackets15 = 0
                for row in df15.iterrows():
                    if row[1]['name'] == 'totalReceivedPackets':
                        totalReceivedPackets15 = int(row[1]['value'])
                    elif row[1]['name'] == 'sentPackets':
                        sentPackets15 += int(row[1]['value'])

                df30 = pd.read_csv('J:/Atieh/University/Internet of things/homeworks/hw3/results/res-30-'+str(sf)+'-'
                                   +str(dbm)+'-'+str(bw)+'.csv')
                totalReceivedPackets30 = 0
                sentPackets30 = 0
                for row in df30.iterrows():
                    if row[1]['name'] == 'totalReceivedPackets':
                        totalReceivedPackets30 = int(row[1]['value'])
                    elif row[1]['name'] == 'sentPackets':
                        sentPackets30 += int(row[1]['value'])
                x = [15, 30]
                y = [totalReceivedPackets15/ sentPackets15, totalReceivedPackets30/sentPackets30]
                plt.plot(x, y)
                plt.xlabel("number of nodes")
                plt.ylabel("Received packets ratio")
                plt.title("sf:" + str(sf) + "-TP:" + str(dbm) + "-BW:" + str(bw))
                plt.show()