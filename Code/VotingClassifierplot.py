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
 0.96200423975268612,
 0.97199202861381429,
 0.97696844230204394,
 0.98223134520541977,
 0.98418210363519232,
 0.9854441169417163,
 0.98619864532776624,
 0.98727735738972311,
 0.98810399213272349,
 0.98908884913957762,
 0.99006069280856646,
 0.99054915357241646,
 0.991111764856486,
 0.991355646555373,
 0.99178077136640397,
 0.99198923242499293,
 0.99159070595076637,
 0.99159305009402954,
 0.99233516888365736,
 0.99180697454578082,
 0.99213946654224616,
 0.99149945809039808,
 0.9923243142889373,
 0.99216580287537948,
 0.9920300577688026,
 0.99307886561470071,
 0.99276682181970721,
 0.99288499237447758],
'Accuracy' : [0.8473092124606334,
 0.84893743524343324,
 0.91714310568757607,
 0.92302308550038625,
 0.92564645606187723,
 0.92618346893916181,
 0.93034759226910901,
 0.93903144743144296,
 0.9412933591045638,
 0.94563532720932619,
 0.94463829724840376,
 0.94590457008567497,
 0.94997467708273331,
 0.95196349987572582,
 0.9540438433402505,
 0.95594331375162889,
 0.95666660005253712,
 0.95476794766266992,
 0.95657589780960284,
 0.95748091589380313,
 0.95630534552151336,
 0.95639522940986588,
 0.95901900924116723,
 0.95847581823643446,
 0.95992341377222634,
 0.96200158857675455,
 0.96290595206610818,
 0.96354005000419252,
 0.96335917724710929,
 0.9667056706458359]}) 

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