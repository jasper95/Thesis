var map, cebuPolygoncebuBounds, rectArr = [], rectCounts = [], height, width, finalResult  = ''
var textFile = null
var utm = "+proj=utm +zone=51", wgs84 = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"
//COORDS
var polygonCoordinates = [
	new google.maps.LatLng(10.489839553833235, 123.89183044433616), 
	new google.maps.LatLng(10.489410400390852, 123.8926925659182), 
	new google.maps.LatLng(10.489480018615836, 123.89324951171909), 
	new google.maps.LatLng(10.490209579467717, 123.89447021484386), 
	new google.maps.LatLng(10.490770339965877, 123.8954696655278), 
	new google.maps.LatLng(10.490790367126579, 123.89617156982467), 
	new google.maps.LatLng(10.4900999069215, 123.89758300781284), 
	new google.maps.LatLng(10.489049911499137, 123.89887237548839), 
	new google.maps.LatLng(10.487890243530387, 123.90012359619163), 
	new google.maps.LatLng(10.486989974975586, 123.90174102783214), 
	new google.maps.LatLng(10.486089706420898, 123.90418243408249), 
	new google.maps.LatLng(10.485679626464787, 123.90648651123058), 
	new google.maps.LatLng(10.485659599304256, 123.90936279296886), 
	new google.maps.LatLng(10.485529899597282, 123.91094207763672), 
	new google.maps.LatLng(10.48561000823986, 123.9125137329105), 
	new google.maps.LatLng(10.485079765319881, 123.91457366943359), 
	new google.maps.LatLng(10.484649658203352, 123.91593170166027), 
	new google.maps.LatLng(10.484000205993652, 123.91694641113281), 
	new google.maps.LatLng(10.48169040679943, 123.91816711425827), 
	new google.maps.LatLng(10.478969573974609, 123.91940307617187), 
	new google.maps.LatLng(10.476200103759879, 123.92051696777378), 
	new google.maps.LatLng(10.474849700927791, 123.92053222656273), 
	new google.maps.LatLng(10.47404956817627, 123.92057037353516), 
	new google.maps.LatLng(10.473190307617244, 123.9208374023442), 
	new google.maps.LatLng(10.472559928894157, 123.92233276367199), 
	new google.maps.LatLng(10.472610473632869, 123.92357635498081), 
	new google.maps.LatLng(10.473270416259822, 123.92436981201172), 
	new google.maps.LatLng(10.473719596862907, 123.9249191284182), 
	new google.maps.LatLng(10.473449707031364, 123.9254302978519), 
	new google.maps.LatLng(10.472920417785701, 123.92603302001953), 
	new google.maps.LatLng(10.47173023223877, 123.92622375488281), 
	new google.maps.LatLng(10.469730377197379, 123.92582702636719), 
	new google.maps.LatLng(10.465419769287109, 123.92533874511719), 
	new google.maps.LatLng(10.461870193481559, 123.92566680908237), 
	new google.maps.LatLng(10.453869819641341, 123.92568969726585), 
	new google.maps.LatLng(10.451629638671932, 123.92569732666016), 
	new google.maps.LatLng(10.434339523315373, 123.92539978027366), 
	new google.maps.LatLng(10.428239822387923, 123.92537689208996), 
	new google.maps.LatLng(10.418820381164664, 123.92505645751953), 
	new google.maps.LatLng(10.414340019226302, 123.92478942871139), 
	new google.maps.LatLng(10.40575027465826, 123.92449188232422), 
	new google.maps.LatLng(10.40299034118658, 123.92445373535202), 
	new google.maps.LatLng(10.401000022888184, 123.92489624023449), 
	new google.maps.LatLng(10.39918041229248, 123.92548370361362), 
	new google.maps.LatLng(10.397060394287223, 123.92585754394565), 
	new google.maps.LatLng(10.384940147400016, 123.92445373535202), 
	new google.maps.LatLng(10.376819610595817, 123.92336273193359), 
	new google.maps.LatLng(10.367859840393066, 123.921630859375), 
	new google.maps.LatLng(10.35758018493658, 123.9201583862307), 
	new google.maps.LatLng(10.354220390319824, 123.91961669921875), 
	new google.maps.LatLng(10.346599578857422, 123.91851043701183), 
	new google.maps.LatLng(10.335900306701888, 123.91620635986374), 
	new google.maps.LatLng(10.335760116577148, 123.91742706298828), 
	new google.maps.LatLng(10.3346204757691, 123.91869354248058), 
	new google.maps.LatLng(10.332830429077262, 123.91934204101562), 
	new google.maps.LatLng(10.331430435180607, 123.92037963867187), 
	new google.maps.LatLng(10.330459594726562, 123.9213485717778), 
	new google.maps.LatLng(10.32859992980957, 123.92265319824219), 
	new google.maps.LatLng(10.327770233154524, 123.92299652099643), 
	new google.maps.LatLng(10.326620101928711, 123.92323303222656), 
	new google.maps.LatLng(10.325519561767692, 123.92314910888672), 
	new google.maps.LatLng(10.324830055237044, 123.9229736328125), 
	new google.maps.LatLng(10.323949813842773, 123.9226913452153), 
	new google.maps.LatLng(10.322629928588867, 123.92307281494186), 
	new google.maps.LatLng(10.321720123291129, 123.92372894287109), 
	new google.maps.LatLng(10.319879531860408, 123.92421722412155), 
	new google.maps.LatLng(10.319219589233455, 123.92417144775391), 
	new google.maps.LatLng(10.319149971008301, 123.92415618896507), 
	new google.maps.LatLng(10.318039894104118, 123.92407989501999), 
	new google.maps.LatLng(10.317139625549316, 123.92395782470737), 
	new google.maps.LatLng(10.31575965881359, 123.92413330078136), 
	new google.maps.LatLng(10.314069747924862, 123.92385101318371), 
	new google.maps.LatLng(10.31317043304449, 123.92344665527389), 
	new google.maps.LatLng(10.312629699707088, 123.92328643798839), 
	new google.maps.LatLng(10.312580108642692, 123.92327880859386), 
	new google.maps.LatLng(10.31210994720459, 123.92314910888672), 
	new google.maps.LatLng(10.311160087585506, 123.92353057861328), 
	new google.maps.LatLng(10.310359954833984, 123.92404174804699), 
	new google.maps.LatLng(10.310139656066838, 123.92420959472702), 
	new google.maps.LatLng(10.309869766235295, 123.92442321777355), 
	new google.maps.LatLng(10.310159683227596, 123.92471313476597), 
	new google.maps.LatLng(10.310660362243709, 123.92517852783214), 
	new google.maps.LatLng(10.310919761657829, 123.92542266845737), 
	new google.maps.LatLng(10.310770034790096, 123.92556762695324), 
	new google.maps.LatLng(10.310390472412166, 123.92582702636719), 
	new google.maps.LatLng(10.309960365295638, 123.92600250244175), 
	new google.maps.LatLng(10.309499740600813, 123.92584991455089), 
	new google.maps.LatLng(10.309080123901367, 123.9254302978519), 
	new google.maps.LatLng(10.308790206909293, 123.92488098144531), 
	new google.maps.LatLng(10.308589935302678, 123.92436218261719), 
	new google.maps.LatLng(10.308369636535758, 123.92392730712891), 
	new google.maps.LatLng(10.308090209961051, 123.92355346679687), 
	new google.maps.LatLng(10.307760238647518, 123.92315673828125), 
	new google.maps.LatLng(10.30731010437006, 123.92278289794922), 
	new google.maps.LatLng(10.306650161743164, 123.92244720459007), 
	new google.maps.LatLng(10.306070327758732, 123.92214202880871), 
	new google.maps.LatLng(10.305999755859489, 123.9218673706057), 
	new google.maps.LatLng(10.305830001831055, 123.92160797119175), 
	new google.maps.LatLng(10.305649757385197, 123.92131805419922), 
	new google.maps.LatLng(10.305600166320801, 123.92108917236362), 
	new google.maps.LatLng(10.305620193481502, 123.92075347900391), 
	new google.maps.LatLng(10.30558013916027, 123.92053222656273), 
	new google.maps.LatLng(10.305459976196403, 123.9201583862307), 
	new google.maps.LatLng(10.305159568786678, 123.91966247558605), 
	new google.maps.LatLng(10.304650306701774, 123.91916656494141), 
	new google.maps.LatLng(10.304059982299748, 123.91863250732445), 
	new google.maps.LatLng(10.303850173950252, 123.9185028076173), 
	new google.maps.LatLng(10.30370044708252, 123.91840362548828), 
	new google.maps.LatLng(10.303339958190975, 123.91815948486374), 
	new google.maps.LatLng(10.303310394287109, 123.91774749755871), 
	new google.maps.LatLng(10.30327033996582, 123.91741180419956), 
	new google.maps.LatLng(10.303259849548397, 123.91735076904342), 
	new google.maps.LatLng(10.303059577942008, 123.91700744628929), 
	new google.maps.LatLng(10.302829742431754, 123.91670989990268), 
	new google.maps.LatLng(10.302740097045898, 123.91658020019577), 
	new google.maps.LatLng(10.302639961242733, 123.9164428710942), 
	new google.maps.LatLng(10.302379608154354, 123.91626739501987), 
	new google.maps.LatLng(10.302089691162223, 123.91607666015659), 
	new google.maps.LatLng(10.301799774169979, 123.9158630371096), 
	new google.maps.LatLng(10.301440238952694, 123.91562652587936), 
	new google.maps.LatLng(10.300999641418457, 123.91539764404297), 
	new google.maps.LatLng(10.300709724426497, 123.91502380371094), 
	new google.maps.LatLng(10.300410270690918, 123.91464996337891), 
	new google.maps.LatLng(10.300239562988395, 123.91426849365234), 
	new google.maps.LatLng(10.300049781799373, 123.91396331787155), 
	new google.maps.LatLng(10.299980163574219, 123.91364288330089), 
	new google.maps.LatLng(10.299860000610408, 123.913330078125), 
	new google.maps.LatLng(10.299790382385254, 123.91319274902366), 
	new google.maps.LatLng(10.29971981048584, 123.91304016113281), 
	new google.maps.LatLng(10.299530029296818, 123.91277313232467), 
	new google.maps.LatLng(10.299340248108024, 123.9125137329105), 
	new google.maps.LatLng(10.299130439758301, 123.9122695922855), 
	new google.maps.LatLng(10.298890113830794, 123.91208648681641), 
	new google.maps.LatLng(10.298640251159611, 123.91197204589844), 
	new google.maps.LatLng(10.298330307006779, 123.91191864013672), 
	new google.maps.LatLng(10.298040390014705, 123.91179656982422), 
	new google.maps.LatLng(10.297760009765739, 123.91171264648437), 
	new google.maps.LatLng(10.297470092773437, 123.91166687011741), 
	new google.maps.LatLng(10.297149658203352, 123.91166687011741), 
	new google.maps.LatLng(10.296730041503906, 123.91161346435547), 
	new google.maps.LatLng(10.296600341796932, 123.91152954101562), 
	new google.maps.LatLng(10.29619026184082, 123.91130065918014), 
	new google.maps.LatLng(10.295929908752385, 123.91087341308605), 
	new google.maps.LatLng(10.29574012756359, 123.91074371337925), 
	new google.maps.LatLng(10.295269966125431, 123.91085052490234), 
	new google.maps.LatLng(10.295009613037223, 123.91084289550781), 
	new google.maps.LatLng(10.294750213623104, 123.91079711914097), 
	new google.maps.LatLng(10.294480323791561, 123.91060638427768), 
	new google.maps.LatLng(10.294159889221305, 123.91040802001987), 
	new google.maps.LatLng(10.293800354003849, 123.91014862060592), 
	new google.maps.LatLng(10.293399810791016, 123.90984344482456), 
	new google.maps.LatLng(10.293129920959473, 123.9096603393557), 
	new google.maps.LatLng(10.293009757995662, 123.90962982177734), 
	new google.maps.LatLng(10.292779922485352, 123.90957641601608), 
	new google.maps.LatLng(10.292389869689998, 123.90937805175804), 
	new google.maps.LatLng(10.292079925537166, 123.90914916992233), 
	new google.maps.LatLng(10.29185962677002, 123.90888977050815), 
	new google.maps.LatLng(10.291689872741927, 123.90862274169967), 
	new google.maps.LatLng(10.291620254516602, 123.90833282470726), 
	new google.maps.LatLng(10.291440010070744, 123.90805816650436), 
	new google.maps.LatLng(10.291370391845817, 123.90776824951172), 
	new google.maps.LatLng(10.291230201721191, 123.90746307373058), 
	new google.maps.LatLng(10.291080474853516, 123.90706634521496), 
	new google.maps.LatLng(10.290880203247127, 123.90663146972656), 
	new google.maps.LatLng(10.290829658508414, 123.90606689453125), 
	new google.maps.LatLng(10.29082012176508, 123.90554809570324), 
	new google.maps.LatLng(10.29076004028343, 123.90509796142578), 
	new google.maps.LatLng(10.290559768676871, 123.90469360351597), 
	new google.maps.LatLng(10.290349960327148, 123.90426635742187), 
	new google.maps.LatLng(10.290390014648437, 123.90379333496094), 
	new google.maps.LatLng(10.290519714355582, 123.90328979492233), 
	new google.maps.LatLng(10.290579795837402, 123.90276336669922), 
	new google.maps.LatLng(10.290679931640682, 123.90225982666016), 
	new google.maps.LatLng(10.29069995880127, 123.90219879150402), 
	new google.maps.LatLng(10.290809631347656, 123.90180206298828), 
	new google.maps.LatLng(10.290849685668945, 123.90138244628952), 
	new google.maps.LatLng(10.290909767150936, 123.90100860595737), 
	new google.maps.LatLng(10.290909767150936, 123.90065002441406), 
	new google.maps.LatLng(10.290829658508414, 123.9002685546875), 
	new google.maps.LatLng(10.290710449218864, 123.89987182617222), 
	new google.maps.LatLng(10.290499687194824, 123.89952087402344), 
	new google.maps.LatLng(10.29020977020275, 123.89919281005859), 
	new google.maps.LatLng(10.28981971740734, 123.89890289306686), 
	new google.maps.LatLng(10.289319992065543, 123.89861297607422), 
	new google.maps.LatLng(10.289259910583496, 123.89856719970703), 
	new google.maps.LatLng(10.288789749145565, 123.8982772827153), 
	new google.maps.LatLng(10.288419723510685, 123.89781188964855), 
	new google.maps.LatLng(10.288330078125, 123.89729309082031), 
	new google.maps.LatLng(10.288330078125, 123.89682769775391), 
	new google.maps.LatLng(10.288379669189396, 123.89644622802734), 
	new google.maps.LatLng(10.288570404052678, 123.89615631103516), 
	new google.maps.LatLng(10.288769721984806, 123.89589691162109), 
	new google.maps.LatLng(10.288869857788086, 123.89560699462936), 
	new google.maps.LatLng(10.288889884948844, 123.89531707763672), 
	new google.maps.LatLng(10.288889884948844, 123.89505767822277), 
	new google.maps.LatLng(10.288889884948844, 123.89476776123081), 
	new google.maps.LatLng(10.288889884948844, 123.89444732666016), 
	new google.maps.LatLng(10.288889884948844, 123.8940887451173), 
	new google.maps.LatLng(10.288889884948844, 123.89392852783226), 
	new google.maps.LatLng(10.288900375366438, 123.8937225341798), 
	new google.maps.LatLng(10.288949966430664, 123.89338684082065), 
	new google.maps.LatLng(10.289030075073242, 123.89308929443359), 
	new google.maps.LatLng(10.289059638977108, 123.89280700683628), 
	new google.maps.LatLng(10.28899955749506, 123.89251708984375), 
	new google.maps.LatLng(10.288869857788086, 123.89225006103516), 
	new google.maps.LatLng(10.288909912109375, 123.89199829101574), 
	new google.maps.LatLng(10.288789749145565, 123.89166259765659), 
	new google.maps.LatLng(10.288550376892317, 123.891151428223), 
	new google.maps.LatLng(10.28826999664318, 123.89066314697277), 
	new google.maps.LatLng(10.28826999664318, 123.88996124267578), 
	new google.maps.LatLng(10.288339614868164, 123.88939666748047), 
	new google.maps.LatLng(10.288619995117301, 123.88864135742187), 
	new google.maps.LatLng(10.288749694824276, 123.88849639892601), 
	new google.maps.LatLng(10.289030075073242, 123.88807678222656), 
	new google.maps.LatLng(10.289310455322379, 123.88751983642612), 
	new google.maps.LatLng(10.289509773254508, 123.88661193847656), 
	new google.maps.LatLng(10.289449691772518, 123.88588714599621), 
	new google.maps.LatLng(10.289449691772518, 123.88584899902344), 
	new google.maps.LatLng(10.289580345153752, 123.88542938232456), 
	new google.maps.LatLng(10.289170265197981, 123.88466644287143), 
	new google.maps.LatLng(10.288960456848088, 123.88424682617187), 
	new google.maps.LatLng(10.288689613342228, 123.88395690917969), 
	new google.maps.LatLng(10.28826999664318, 123.88368988037109), 
	new google.maps.LatLng(10.288109779357853, 123.88371276855503), 
	new google.maps.LatLng(10.287579536438102, 123.88375854492187), 
	new google.maps.LatLng(10.287520408630371, 123.88398742675793), 
	new google.maps.LatLng(10.287500381469783, 123.88403320312534), 
	new google.maps.LatLng(10.287919998169059, 123.88424682617187), 
	new google.maps.LatLng(10.288000106811637, 123.88446807861362), 
	new google.maps.LatLng(10.288060188293457, 123.88466644287143), 
	new google.maps.LatLng(10.288200378418026, 123.88466644287143), 
	new google.maps.LatLng(10.288339614868164, 123.88487243652366), 
	new google.maps.LatLng(10.288689613342228, 123.88514709472668), 
	new google.maps.LatLng(10.288689613342228, 123.88578033447266), 
	new google.maps.LatLng(10.288479804992733, 123.88688659668014), 
	new google.maps.LatLng(10.288129806518612, 123.88730621337891), 
	new google.maps.LatLng(10.287919998169059, 123.88745117187545), 
	new google.maps.LatLng(10.287369728088379, 123.88773345947288), 
	new google.maps.LatLng(10.286959648132438, 123.88773345947288), 
	new google.maps.LatLng(10.286540031433333, 123.88787078857422), 
	new google.maps.LatLng(10.286199569702148, 123.887939453125), 
	new google.maps.LatLng(10.28577995300293, 123.887939453125), 
	new google.maps.LatLng(10.285280227661076, 123.88722229003918), 
	new google.maps.LatLng(10.284999847412109, 123.88694763183628), 
	new google.maps.LatLng(10.283060073852596, 123.88500213623047), 
	new google.maps.LatLng(10.282779693603572, 123.88500213623047), 
	new google.maps.LatLng(10.28092002868658, 123.8831481933596), 
	new google.maps.LatLng(10.280830383300724, 123.88305664062523), 
	new google.maps.LatLng(10.279379844665584, 123.88233184814453), 
	new google.maps.LatLng(10.277999877929687, 123.88176727294922), 
	new google.maps.LatLng(10.27672004699707, 123.88112640380871), 
	new google.maps.LatLng(10.276619911193961, 123.88108062744141), 
	new google.maps.LatLng(10.274820327758789, 123.88086700439476), 
	new google.maps.LatLng(10.274060249328727, 123.88094329833996), 
	new google.maps.LatLng(10.273440361023063, 123.88128662109375), 
	new google.maps.LatLng(10.27332973480236, 123.88155364990268), 
	new google.maps.LatLng(10.273159980773926, 123.88198089599621), 
	new google.maps.LatLng(10.273159980773926, 123.88240051269531), 
	new google.maps.LatLng(10.273099899292049, 123.88260650634766), 
	new google.maps.LatLng(10.272890090942383, 123.88288879394565), 
	new google.maps.LatLng(10.271920204162598, 123.88282012939499), 
	new google.maps.LatLng(10.271439552307186, 123.88260650634766), 
	new google.maps.LatLng(10.271089553833065, 123.88246917724621), 
	new google.maps.LatLng(10.270540237426871, 123.88204956054687), 
	new google.maps.LatLng(10.270469665527401, 123.88198089599621), 
	new google.maps.LatLng(10.268349647522029, 123.88046264648472), 
	new google.maps.LatLng(10.267769813537598, 123.88002777099643), 
	new google.maps.LatLng(10.267219543457088, 123.87967681884766), 
	new google.maps.LatLng(10.266739845275822, 123.87940216064464), 
	new google.maps.LatLng(10.266249656677303, 123.87885284423839), 
	new google.maps.LatLng(10.265839576721191, 123.87848663330124), 
	new google.maps.LatLng(10.265279769897518, 123.8782882690432), 
	new google.maps.LatLng(10.264590263366756, 123.87808227539074), 
	new google.maps.LatLng(10.264180183410588, 123.87779998779331), 
	new google.maps.LatLng(10.264149665832633, 123.87772369384811), 
	new google.maps.LatLng(10.26403999328619, 123.87744903564453), 
	new google.maps.LatLng(10.263759613037053, 123.87689208984375), 
	new google.maps.LatLng(10.263070106506461, 123.87619781494186), 
	new google.maps.LatLng(10.262129783630314, 123.87561798095726), 
	new google.maps.LatLng(10.262060165405387, 123.87296295166061), 
	new google.maps.LatLng(10.261859893798771, 123.86766815185547), 
	new google.maps.LatLng(10.261949539184684, 123.86570739746139), 
	new google.maps.LatLng(10.262559890747184, 123.86428833007812), 
	new google.maps.LatLng(10.263030052185172, 123.86319732666027), 
	new google.maps.LatLng(10.263930320739803, 123.8618621826173), 
	new google.maps.LatLng(10.266550064087028, 123.85739135742222), 
	new google.maps.LatLng(10.269399642944336, 123.85339355468773), 
	new google.maps.LatLng(10.269820213317871, 123.85308837890636), 
	new google.maps.LatLng(10.270560264587402, 123.85282135009788), 
	new google.maps.LatLng(10.27190017700201, 123.85254669189499), 
	new google.maps.LatLng(10.273859977722111, 123.85180664062534), 
	new google.maps.LatLng(10.274860382080078, 123.85119628906261), 
	new google.maps.LatLng(10.275830268859863, 123.85057830810547), 
	new google.maps.LatLng(10.276769638061637, 123.84966278076183), 
	new google.maps.LatLng(10.278249740600643, 123.84812927246105), 
	new google.maps.LatLng(10.279069900512752, 123.84641265869152), 
	new google.maps.LatLng(10.279230117797852, 123.84394836425793), 
	new google.maps.LatLng(10.279999732971248, 123.84297943115246), 
	new google.maps.LatLng(10.280540466308651, 123.84130859375034), 
	new google.maps.LatLng(10.283029556274414, 123.83966827392601), 
	new google.maps.LatLng(10.294380187988224, 123.82967376709018), 
	new google.maps.LatLng(10.296540260314941, 123.82804107666016), 
	new google.maps.LatLng(10.307359695434684, 123.81974029541061), 
	new google.maps.LatLng(10.308670043945426, 123.82029724121105), 
	new google.maps.LatLng(10.309749603271484, 123.8208465576173), 
	new google.maps.LatLng(10.311240196228255, 123.82164001464866), 
	new google.maps.LatLng(10.312529563903809, 123.82240295410179), 
	new google.maps.LatLng(10.314160346984863, 123.82241821289108), 
	new google.maps.LatLng(10.315910339355582, 123.82290649414062), 
	new google.maps.LatLng(10.317259788513184, 123.82405853271484), 
	new google.maps.LatLng(10.320139884948787, 123.82491302490268), 
	new google.maps.LatLng(10.32161998748785, 123.82450866699264), 
	new google.maps.LatLng(10.324549674987907, 123.823486328125), 
	new google.maps.LatLng(10.327170372009221, 123.82067108154308), 
	new google.maps.LatLng(10.328180313110295, 123.81951141357433), 
	new google.maps.LatLng(10.328080177307356, 123.81902313232422), 
	new google.maps.LatLng(10.327790260314885, 123.81880950927768), 
	new google.maps.LatLng(10.327139854431266, 123.81849670410179), 
	new google.maps.LatLng(10.326669692993107, 123.81802368164108), 
	new google.maps.LatLng(10.326919555664119, 123.81720733642624), 
	new google.maps.LatLng(10.327260017395133, 123.81655883789074), 
	new google.maps.LatLng(10.328419685363883, 123.81494903564464), 
	new google.maps.LatLng(10.328229904174918, 123.8144683837894), 
	new google.maps.LatLng(10.327839851379508, 123.81411743164062), 
	new google.maps.LatLng(10.326939582824707, 123.81317901611328), 
	new google.maps.LatLng(10.326910018921012, 123.81244659423874), 
	new google.maps.LatLng(10.327260017395133, 123.81204986572266), 
	new google.maps.LatLng(10.326339721679915, 123.803466796875), 
	new google.maps.LatLng(10.328450202941838, 123.791259765625), 
	new google.maps.LatLng(10.328370094299316, 123.79057312011753), 
	new google.maps.LatLng(10.328189849853629, 123.7897872924807), 
	new google.maps.LatLng(10.327719688415641, 123.78897094726562), 
	new google.maps.LatLng(10.326319694519043, 123.78527832031261), 
	new google.maps.LatLng(10.326009750366211, 123.7846374511721), 
	new google.maps.LatLng(10.325550079345817, 123.78267669677734), 
	new google.maps.LatLng(10.325770378112793, 123.7812118530278), 
	new google.maps.LatLng(10.326729774475154, 123.77056884765625), 
	new google.maps.LatLng(10.333219528198356, 123.77142333984375), 
	new google.maps.LatLng(10.340029716491642, 123.77226257324253), 
	new google.maps.LatLng(10.349209785461539, 123.77292633056641), 
	new google.maps.LatLng(10.356080055236816, 123.77240753173839), 
	new google.maps.LatLng(10.361180305481014, 123.77216339111328), 
	new google.maps.LatLng(10.364370346069336, 123.7717437744144), 
	new google.maps.LatLng(10.369230270385799, 123.77169799804722), 
	new google.maps.LatLng(10.372529983520565, 123.77169036865268), 
	new google.maps.LatLng(10.376790046691951, 123.77194976806663), 
	new google.maps.LatLng(10.379220008850154, 123.7718887329105), 
	new google.maps.LatLng(10.383000373840275, 123.77153778076172), 
	new google.maps.LatLng(10.385649681091365, 123.77098846435581), 
	new google.maps.LatLng(10.388279914856014, 123.77027130126953), 
	new google.maps.LatLng(10.390640258789119, 123.76973724365246), 
	new google.maps.LatLng(10.395870208740291, 123.77474212646518), 
	new google.maps.LatLng(10.407179832458723, 123.78643798828159), 
	new google.maps.LatLng(10.418120384216422, 123.79760742187523), 
	new google.maps.LatLng(10.418769836425781, 123.79741668701195), 
	new google.maps.LatLng(10.419690132141113, 123.7972564697269), 
	new google.maps.LatLng(10.420680046081657, 123.7977294921875), 
	new google.maps.LatLng(10.422189712524528, 123.79818725585983), 
	new google.maps.LatLng(10.422639846801758, 123.79834747314464), 
	new google.maps.LatLng(10.423729896545353, 123.79878234863315), 
	new google.maps.LatLng(10.424839973449707, 123.79962158203125), 
	new google.maps.LatLng(10.42588996887207, 123.80032348632812), 
	new google.maps.LatLng(10.426750183105412, 123.80081939697277), 
	new google.maps.LatLng(10.427189826965389, 123.80075836181663), 
	new google.maps.LatLng(10.427029609680289, 123.80169677734409), 
	new google.maps.LatLng(10.427040100097884, 123.8026123046875), 
	new google.maps.LatLng(10.428009986877498, 123.80372619628952), 
	new google.maps.LatLng(10.429579734802189, 123.80502319335949), 
	new google.maps.LatLng(10.429949760437069, 123.80587768554699), 
	new google.maps.LatLng(10.430939674377555, 123.80642700195312), 
	new google.maps.LatLng(10.431630134582463, 123.80683898925815), 
	new google.maps.LatLng(10.43229961395275, 123.80760192871128), 
	new google.maps.LatLng(10.433329582214355, 123.80815887451172), 
	new google.maps.LatLng(10.435159683227653, 123.80899810791016), 
	new google.maps.LatLng(10.436579704284668, 123.81067657470726), 
	new google.maps.LatLng(10.437410354614315, 123.81231689453159), 
	new google.maps.LatLng(10.43867015838623, 123.81372833251976), 
	new google.maps.LatLng(10.439040184021223, 123.81524658203148), 
	new google.maps.LatLng(10.440099716186523, 123.81658935546898), 
	new google.maps.LatLng(10.440879821777344, 123.81765747070347), 
	new google.maps.LatLng(10.441800117492676, 123.81944274902366), 
	new google.maps.LatLng(10.441450119018555, 123.82015228271484), 
	new google.maps.LatLng(10.441439628601131, 123.82121276855514), 
	new google.maps.LatLng(10.442299842834529, 123.82142639160168), 
	new google.maps.LatLng(10.44369029998785, 123.82405853271484), 
	new google.maps.LatLng(10.444680213928336, 123.82602691650413), 
	new google.maps.LatLng(10.445759773254338, 123.82698059082054), 
	new google.maps.LatLng(10.446559906005859, 123.82736968994186), 
	new google.maps.LatLng(10.447600364685115, 123.828369140625), 
	new google.maps.LatLng(10.448699951171875, 123.83054351806641), 
	new google.maps.LatLng(10.450180053711051, 123.83260345459007), 
	new google.maps.LatLng(10.451649665832633, 123.83467102050781), 
	new google.maps.LatLng(10.453129768371639, 123.83682250976562), 
	new google.maps.LatLng(10.453920364379883, 123.83775329589866), 
	new google.maps.LatLng(10.455679893493766, 123.83953857421886), 
	new google.maps.LatLng(10.473600387573356, 123.86274719238304), 
	new google.maps.LatLng(10.493430137634391, 123.88881683349609), 
	new google.maps.LatLng(10.49225997924799, 123.88957214355503), 
	new google.maps.LatLng(10.491000175476131, 123.89057159423862), 
	new google.maps.LatLng(10.489839553833235, 123.89183044433616)			
	]

$(document).ready(function () {

	$('#bRead-file').on('click', function(e){
		e.preventDefault()
		var files = $('#file').prop("files")
		read(files, 0) //read the first file
	})

	//read file
	function read(files, ctr){
		var file = files[ctr]
	    var reader = new FileReader()
	    reader.onload = function(e) {  
	        processData(e, files, ctr) 
	    }
	    reader.readAsText(file, "UTF-8")
	}
	
	//process the data of each file
	function processData(e, files, ctr){
        var week1DOutput = ''
        var non_zero2 = 0
        var weeklyCounts = createNew2DArray()
		var data = e.target.result.split('\n')
		for(var i=0; i<data.length-1; i++){
        	var example = data[i].split(' ')
        	var x_y = proj4(utm,wgs84,[example[2], example[3]])
        	findAndIncrementGridCount(new google.maps.LatLng(x_y[1], x_y[0]), weeklyCounts)
    	}
    	for(var i=0; i<height; i++){
    		for(var j=0; j<width; j++){
    			var space = (j === height-1 && i === width-1) ? '' : ' '
    			week1DOutput += weeklyCounts[i][j] + space
    			if(weeklyCounts[i][j] > 0) non_zero2++
    		}
		}
		console.log(non_zero2)
		finalResult += week1DOutput+'\n'	
    	if(ctr < files.length-1)
    		read(files, ctr+1)
    	else{
    		$('#lDownload').attr('href', makeFile(finalResult))
    		$('#lDownload').show()
    	} 
	}

	//makes text files for the output
	function makeFile(output){
		var data = new Blob([output], {type: 'text/plain'})
		if(textFile !== null)
			window.URL.revokeObjectURL(textFile)
		textFile = window.URL.createObjectURL(data);
		return textFile	
	}

	//finds the point's grid and increment the grid count 
	function findAndIncrementGridCount(point, rectCounts_copy){
		outer:
		for(var i=0; i<height; i++)
			for(var j=0; j<width; j++)
				if(rectArr[i][j].getBounds().contains(point)){
					rectCounts_copy[i][j]++
					break outer
				}
	}

	//initialize and draw cebu bounds and polygon
	function initAndDrawCebuBoundsAndPolygon(){
        var cebuCenter = new google.maps.LatLng(10.3224,123.8985);
        var mapOptions = {
            zoom: 10,
            center: cebuCenter,
            mapTypeId: google.maps.MapTypeId.TERRAIN
        };
        map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions)
        cebuPolygon = new google.maps.Polygon({
            paths: polygonCoordinates,
            strokeColor: "#FF0000",
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: "#6666FF",
            fillOpacity: 0.00
        })
        cebuPolygon.setMap(map);
       	cebuBounds = new google.maps.Rectangle({
		    strokeColor: '#FF0000',
		    strokeOpacity: 0.00,
		    strokeWeight: 4,
		    fillColor: '#FF0000',
		    fillOpacity: 0.00,
		    map: map,
		    bounds: {
	       		north: 10.498277,
	       		south: 10.2594266,
	       		east: 123.9291998,
	    	   	west: 123.7633896
	    	}
	   	})

   	}

   	//initialize and draw the grids overlay 
   	function initAndDrawGird (cellSize) {
        var NE = new google.maps.LatLng(10.498277, 123.9291998);
        var S = google.maps.geometry.spherical.computeOffset(NE,cellSize,180)
        var SW = google.maps.geometry.spherical.computeOffset(S,cellSize,270)  
        var h_lim, w_lim, NE2
        for(var i = 0; ;i++){
            NEtemp = google.maps.geometry.spherical.computeOffset(NE, i*cellSize, 180)
            SWtemp = google.maps.geometry.spherical.computeOffset(SW, i*cellSize, 180)
            if( !(cebuBounds.getBounds().contains(NEtemp) || cebuBounds.getBounds().contains(SWtemp)) ){
                h_lim = height = i;
                break;
            }
            var subl = []
            for(var k=0; ;k++){
        		var rectangle = new google.maps.Rectangle()
                var rectOptions = {
                    strokeColor: "#FF0000",
                    strokeOpacity: 0.3,
                    strokeWeight: 2,
                    fillOpacity: 0.00,
                    map: map,
                    bounds: new google.maps.LatLngBounds(SWtemp,NEtemp)
                };
                rectangle.setOptions(rectOptions)
            	subl.push(rectangle)
                var NEtemp = google.maps.geometry.spherical.computeOffset(NEtemp,cellSize,270)
                var SWtemp = google.maps.geometry.spherical.computeOffset(SWtemp,cellSize,270)
                if( !(cebuBounds.getBounds().contains(NEtemp) || cebuBounds.getBounds().contains(SWtemp)) ){
                    if(i == 0){
                    	w_lim = width = k
                    	NE2 = NEtemp
                    }
                    rectArr.push(subl)
                    break
                }
            }
        }
        console.log(height+' '+width)
    }
    function createNew2DArray(){
    	var newArray =  []
    	for(var i=0; i<height; i++)
    		newArray.push(Array.apply(null, Array(width)).map(Number.prototype.valueOf,0))
    	return newArray
    }
   	initAndDrawCebuBoundsAndPolygon()
   	initAndDrawGird(500)
});