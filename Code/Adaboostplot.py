import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd

width = 0.35

#columns = [1...30]
#columns = ['having_IP_Address','URL_Length','Shortining_Service','having_At_Symbol','double_slash_redirecting','Prefix_Suffix','having_Sub_Domain','SSLfinal_State','Domain_registeration_length','Favicon','port','HTTPS_token','Request_URL','URL_of_Anchor','Links_in_tags','SFH','Submitting_to_email','Abnormal_URL','Redirect','on_mouseover','RightClick','popUpWidnow','Iframe','age_of_domain','DNSRecord','web_traffic','Page_Rank','Google_Index','Links_pointing_to_page','Statistical_report']
#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(30)
m1_t = pd.DataFrame({ 'AUC': [0.87582846685831461,
 0.89804741322729564,
 0.96160254149038749,
 0.97067224864044677,
 0.9741857016276253,
 0.97559736345670578,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536,
 0.97875601991405536],
'Accuracy' : [0.84730904999171353,
 0.84893727259539542,
 0.91732328446743383,
 0.92012693003380563,
 0.92465040891385852,
 0.9158736432505159,
 0.92600573893760885,
 0.92600573893760885,
 0.92600573893760885,
 0.92600573893760885,
 0.92600573893760885,
 0.92600573893760885,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616,
 0.92130070817394616]}) 

#@m1_t[['abnormal','fix','normal']].plot(kind='bar', width = width)
#ax = m1_t['bad_rate'].plot(secondary_y=True)
m1_t[['AUC']].plot(kind='bar')
m1_t['Accuracy'].plot(kind='line',color = "red")


ax = plt.gca()
plt.xlim([-width, len(m1_t['Accuracy'])-width])
plt.xlabel('Number of features selected')
plt.ylabel('AUC')
ax.set_xticklabels(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'))
plt.ylim(0.8,1)
plt.show()