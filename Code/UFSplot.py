import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd

width = 0.35

#columns = [1...30]
#columns = ['having_IP_Address','URL_Length','Shortining_Service','having_At_Symbol','double_slash_redirecting','Prefix_Suffix','having_Sub_Domain','SSLfinal_State','Domain_registeration_length','Favicon','port','HTTPS_token','Request_URL','URL_of_Anchor','Links_in_tags','SFH','Submitting_to_email','Abnormal_URL','Redirect','on_mouseover','RightClick','popUpWidnow','Iframe','age_of_domain','DNSRecord','web_traffic','Page_Rank','Google_Index','Links_pointing_to_page','Statistical_report']
#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(30)
m1_t = pd.DataFrame({ 'AUC': [0.882073843894
,
 0.905677413218
,
 0.90278348091
,
 0.91884517515
,
 0.917173606872
,
 0.919657970601
,
 0.922130179391
,
 0.92359088591
,
 0.932770771072
,
 0.934799853084
,
 0.931759268801
,
 0.932349047555
,
 0.934540107333
,
 0.933598892315
,
 0.933999212571
,
 0.934989311581
,
 0.936780051104
,
 0.937250658613
,
 0.9364500181
,
 0.937650978869
,
 0.937791553375
,
 0.937981011872
,
 0.939582292897
,
 0.940172071651
,
 0.938781652385
,
 0.938451619381
,
 0.941415838942
,
 0.941415838942
,
 0.939765673925],
'Accuracy' : [ 0.885672937771
,
 0.908465991317
,
 0.906295224313
,
 0.921128798842
,
 0.919681620839
,
 0.924023154848
,
 0.926193921852
,
 0.927641099855
,
 0.93523878437
,
 0.937771345876
,
 0.934515195369
,
 0.93523878437
,
 0.937409551375
,
 0.936685962373
,
 0.937047756874
,
 0.938133140376
,
 0.93994211288
,
 0.940303907381
,
 0.939580318379
,
 0.940665701881
,
 0.940665701881
,
 0.941027496382
,
 0.942474674385
,
 0.943198263386
,
 0.941751085384
,
 0.941389290883
,
 0.943560057887
,
 0.943560057887
,
 0.941751085384]}) 

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