import matplotlib.pyplot as plt
Info =  ['Gold','Silver','Bronze','Total']
Australia = [80,59,59,198]
India = [26,20,20,66]
# plt.bar(Info,Australia, label="Australia")
# plt.bar(Info,India,color='k', label="India")
# plt.legend()
# plt.xlabel("Medal Type")
# plt.ylabel("Australia, India Medal Count")

contri = [17,8.8,12.75,14]
houses = ['Vidya', 'Kshama', 'Namrata', 'Karuna']
expl = [0,.1,0,0]
plt.pie(contri,colors = ['c','k','m','y'], labels=houses, explode=expl, autopct = "%1.0f%%")
# plt.hist(India, bins=20)
