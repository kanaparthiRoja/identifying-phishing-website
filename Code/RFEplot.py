import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd

width = 0.35

#columns = [1...30]
#columns = ['having_IP_Address','URL_Length','Shortining_Service','having_At_Symbol','double_slash_redirecting','Prefix_Suffix','having_Sub_Domain','SSLfinal_State','Domain_registeration_length','Favicon','port','HTTPS_token','Request_URL','URL_of_Anchor','Links_in_tags','SFH','Submitting_to_email','Abnormal_URL','Redirect','on_mouseover','RightClick','popUpWidnow','Iframe','age_of_domain','DNSRecord','web_traffic','Page_Rank','Google_Index','Links_pointing_to_page','Statistical_report']
#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(30)
m1_t = pd.DataFrame({ 'AUC': [0.837631953748
,
0.839282118764
,
0.912369763798
,
0.917525043137
,
0.918661794122
,
0.921323461409
,
0.922243273166
,
0.92355732771
,
0.925937845986
,
0.926316762981
,
0.929427634517
,
0.928486419499
,
0.933128284806
,
0.932538506052
,
0.932489622061
,
0.935081002095
,
0.933739466821
,
0.933360549826
,
0.935340747846
,
0.933479721071
,
0.934491223342
,
0.934891543598
,
0.934891543598
,
0.935903045869
,
0.938234680153
,
0.941556413448
,
0.941886446451
,
0.94235705396
,
0.942757374216
,
0.940966634694],
'Accuracy' : [0.852749638205
,
0.854558610709
,
0.915340086831
,
0.919681620839
,
0.921852387844
,
0.924384949349
,
0.925470332851
,
0.925832127352
,
0.928364688857
,
0.929088277858
,
0.932344428365
,
0.931620839363
,
0.936324167873
,
0.935600578871
,
0.93523878437
,
0.937771345876
,
0.936685962373
,
0.935962373372
,
0.938133140376
,
0.936324167873
,
0.937047756874
,
0.937409551375
,
0.937409551375
,
0.938133140376
,
0.940303907381
,
0.943560057887
,
0.943921852388
,
0.944283646889
,
0.944645441389
,
0.942836468886]}) 

#@m1_t[['abnormal','fix','normal']].plot(kind='bar', width = width)
#ax = m1_t['bad_rate'].plot(secondary_y=True)
m1_t[['AUC']].plot(kind='bar')
m1_t['Accuracy'].plot(kind='line',color = "red")


ax = plt.gca()
plt.xlim([-width, len(m1_t['Accuracy'])-width])
ax.set_xticklabels(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'))
plt.xlabel('Number of features selected')
plt.ylabel('AUC')
plt.ylim(0.8,1)
plt.show()