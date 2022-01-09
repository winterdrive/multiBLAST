#kuofile做完之後拿testo的2000多條來比
import linecache as lc
from numpy.lib.shape_base import split
import pandas as pd
import csv
from os import path,listdir

Load_file_dir="C:/PYTHON/Download_Seq_files/gb_csv/Polypodiopsida/"
Save_file_dir=""

filename=[]
files = listdir(Load_file_dir)
# 以迴圈處理
for f in files:
  # 產生檔案的絕對路徑
  fullpath = Load_file_dir + f
  # 判斷 fullpath 是檔案還是目錄
  if path.isfile(fullpath):
    #print("檔案：", f)
    filename.append(f[:-7])
  #elif isdir(fullpath):
    # print("目錄：", f)#這裡不需要，因為不是夾中夾
#print(filename)
# "C:/PYTHON/Download_Seq_files/gb_csv/Polypodiopsida/"有7646個檔
#現在有Polypodiopsida的檔案清單"filename"了


#接著要來把csv合併起來，
#應該得用pd了

testo=["JX535916","JX535914","JX535915","KM106046","FJ807658","AF515230","KT804996","AF469791","AF469792","AF469788","AF469793","AF469794","AF469789","AF469787","AF469790","AF469795","AF469796","JF980695","JN052907","JF980639","JF980662","KP637258","JF980649","JF980681","LC004381","JF980696","JF980659","JF980702","JF980637","LC004387","JF980682","JF980656","JF980663","JF980652","JF980697","JF980698","JF980664","LC004392","JF980657","JF980693","JF980651","JF980661","JF980653","KJ779993","JF980648","KP637262","JF980660","JN052898","JN052918","JF980634","KP637265","LC004397","JF980701","LC004379","KJ779988","JF980643","LC004395","KP637270","JF980700","LC004398","JF980699","JF980692","AY459176","EU571226","AY529465","AY529466","AY529467","AY529468","AY529470","AY529471","AY529472","AY529473","AY529474","JN654969","KM106048","JN654970","GU476718","JN654967","GU476712","JN654965","DQ432677","KP085534","KP085525","DQ432671","DQ432678","KP085526","DQ432672","DQ432673","DQ432668","KP085519","KP085522","KP137492","KP085520","KP085521","KP085524","KP085533","DQ432666","KP085523","AM689621","AY534747","AM410316","AM410336","AM410318","KJ438925","AM410324","AM410306","AM689675","AM410329","KR153995","AM410337","AM410305","AM410323","AM410300","AM410338","AM410325","AM410326","KT804998","KT805000","KT805004","AF425125","KT805007","KT805010","KT805013","KT805015","KT805017","DQ845241","AF448928","AF448930","AF448925","AF448922","AF448923","DQ845242","AF448924","AF448926","AF448931","DQ838082","EU221806","DQ838086","DQ838077","DQ838087","EU221807","DQ838078","DQ838080","DQ838083","DQ838081","EU221810","AY651836","DQ838079","EU221871","DQ838075","DQ838076","DQ838085","KM884745","JN869326","JX040524","JN869323","LC004400","KM884761","KM884763","JN869329","JN869331","KM884754","KM884756","KM884757","JX040523","KM884760","KM884767","AY268782","DQ514480","DQ514481","KJ464593","DQ514482","DQ514483","EU106593","KC896602","DQ514484","DQ514485","AF515242","EF540700","AY736356","DQ838074","DQ914209","EU831181","DQ914210","DQ914211","DQ914212","GU376565","GU376569","JQ700454","JQ700455","JQ700457","JQ700462","JQ700465","EU128516","KF897940","KC977411","KC977416","KF897941","KC977420","KC977419","KC977425","KC977412","KC977423","KC977424","GU476674","GU476702","GU476704","GU476708","GU476709","GU476710","GU476714","GU476690","GU387285","GU476723","GU476728","GU476730","GU476731","DQ914213","DQ914214","AY300049","JX068725","AY300050","KP835385","AY300051","KP835372","AY300052","AY300053","AY300054","EU240028","KP851900","KP835399","AF525258","AF240667","KP835357","AY549863","KP218786","KP861409","KP835370","AY300055","GQ377138","AY300056","KP639686","KP218784","KP835374","JQ767821","KP835387","AF516263","AY283207","GQ377147","AY159292","AY549834","KP639691","JX475140","KP835400","JX068727","AY300058","AY162336","AF525254","AY300059","KP835352","AY549840","AY641794","AY641808","KP851901","AY549857","AF525243","AY300060","AF525244","JQ767830","KP835396","AY300061","KP851902","KP835363","KR233937","AY549848","AY549836","AY549860","AY300064","KP835378","KP835371","JQ724224","JQ767851","KP835375","AY158241","JQ364897","JQ767855","AY549874","JX068749","AY549839","EF418323","AY300067","AF525250","AY549852","KP851903","AY300068","AF525245","KP835403","AY549851","AY538185","KP639690","KP639696","KP835394","AF525257","KP639699","AY300069","AY549853","AY549835","AY538180","GU017743","AY300071","KP835365","AF240662","EU240030","AY300072","AY300073","AY300074","KP835367","KP835393","KP872962","AY538178","KP639689","AY300076","AY538175","AY300077","AY161003","KP835361","JQ724225","AY300078","KP218808","JQ767908","JX068750","AF525259","KP835395","AF525260","KP888649","KP835386","AF525249","AY164262","KP835359","AF525240","KP639698","KP835362","JQ767912","JX475142","AY549858","AY549856","AY300082","AF515243","JF950902","AY162340","JQ767931","AY300083","AY300085","AY300084","JX068763","AF240661","AY300086","AF525247","KP835350","AY538181","HQ676518","AY300087","AF525248","AY300088","KP639688","AY641799","AY300089","AY300090","JQ767934","AY300091","KP835347","KP835360","KP835377","JX068745","EU240029","KP835346","KP835356","AY300070","AY549832","AY549871","AY300093","KP835348","EF645604","AY300095","KP851919","AY549833","AY300096","EU831182","EU831184","DQ914218","EU831185","KJ196643","AF514835","KP979036","EU329069","EU329070","HM156336","AF514834","FJ821327","FJ821325","KP979046","EU329072","FJ821320","FJ807659","EU329073","EU329074","AY300047","JN673871","AF515239","EU329075","FJ821329","HQ676519","AF515258","AF515254","EU329079","EU329080","EU329081","FJ821332","FJ821321","EU329084","AF515256","FJ821330","EU329086","AF515236","AF514833","FJ821324","EU329088","EU329089","EU329090","FJ821319","FJ821322","EU329091","AF515234","FJ821328","EU329093","EU329094","AF515231","EU329096","AF515259","EU329098","FJ821326","EF520882","JX273520","JX273535","DQ066508","DQ066515","EF520888","EF520890","EF520893","KJ170840","DQ683373","KJ170841","JQ907366","JQ907367","JQ907368","DQ683375","KF975732","DQ683436","KJ170842","KJ170843","KJ170844","KM001891","KM001892","DQ683380","KF975714","KF975715","JQ907370","KF591318","KJ170858","KM001893","KF975716","KJ170859","DQ683384","JQ907371","DQ683386","KF591340","JQ907372","DQ683391","JF950939","KM001898","KF975717","KJ170846","KF975718","JF950940","DQ683426","JQ907373","JQ907374","KM001894","KF975719","KJ170860","JQ907375","JQ907376","KF975733","KF975720","DQ683393","JQ907377","KF975721","KJ170847","JQ907378","DQ683428","DQ683398","KF975722","JQ907379","KJ170862","KJ170863","DQ683400","DQ683424","DQ683402","KF591326","KJ170848","KF975723","KM001895","KF975724","KF975725","KF975727","KJ170864","KJ170849","KJ170851","KF975728","KM001896","KF591331","DQ683412","KJ170866","JQ907381","JQ907382","JQ907384","EF427634","KJ170865","KM001897","JQ907388","KF975729","JQ907389","DQ683415","KF975730","KF975731","KJ170852","KJ170853","KJ170854","KJ170855","DQ683430","GU376501","GU376502","GU376509","GU376503","GU376530","GU376510","GU376511","GU376515","GU376516","GU376517","GU376518","GU376524","GU376525","GU376526","GU376528","GU376529","GU376531","DQ849119","DQ849123","AY138422","KF700390","AY138426","DQ849189","AY138431","DQ849131","DQ849134","DQ849136","AY138432","AY138425","KF700427","KF700432","AY138429","DQ849170","DQ849173","AY138434","AY138433","AY138428","AY138427","AY138423","AY138440","KF700450","DQ849184","KF700453","AY138444","KF700455","DQ432686","AM410354","KM106049","GU476618","KM106050","KM106052","EF104510","AY083647","EF104511","EF104512","EF104513","AY083648","EF104514","AY083649","EF104515","GU476624","KM106053","KM106054","KM106055","GU476625","GU476626","KM106056","GU476619","KM106057","KM106058","GU476621","GU935581","DQ432665","DQ432667","KP085532","DQ432679","DQ432664","DQ432675","GU935593","GU935607","GU935590","GU935582","JF980688","JN122018","DQ432669","GU935580","DQ432674","GU935612","GU935588","GU935597","DQ432676","GU935578","GU935586","GU935596","GU935583","DQ432670","DQ432662","KP085529","GU935591","GU935609","EU831190","DQ914231","KP085527","KP085528","JN122019","GU935601","AF425126","KT805019","AF425128","JN572235","KT805020","JN572237","KT805021","KT805022","JN572239","JN572240","JN572244","KT805023","JN572246","JN572247","JN572248","KT805024","EU221811","EU128512","EU128514","JF514048","KM106059","JX485683","JX485684","JX485685","JX485686","JX485687","JX485688","JX485689","KF955995","GU476631","KM106060","JF514044","KF570110","EU483044","EU483045","EU483046","EU483047","GQ256171","EU483055","JX103780","EU483061","EU483049","EU483050","DQ432690","AB277814","EU329105","AF515246","JN572252","KT805025","JN572255","AF425129","JN189136","DQ432692","JN189135","DQ432691","KF897948","KF709509","KJ196655","KJ196715","JF514047","AM689623","AM689624","AM689625","AM689626","AM410314","AM689632","AM689636","JF950907","AM410351","AM689647","AM689648","AM410339","AM689654","AM410321","AM410315","AM689663","AM689666","AM410352","AM410330","AM689668","AM410345","AM410302","AM689671","AM689673","AM410320","AM410308","AM689676","AM410349","AM689679","AM689680","AM410343","AM689681","AM689683","AM410335","AM689684","AM689685","AM689686","AM689687","AM689688","KR153994","AM410322","AM410348","AM410319","AM689689","AM410328","AM689650","AM689653","AM410344","AM410346","AM689690","AM410332","AM689692","AM689693","AM689694","AM410331","AM410347","AM689701","AM410350","AM689702","AM689704","DQ514487","JN572257","JN572258","DQ514488","KT805026","JN572241","JN572245","AY736346","AY736347","AY736339","AY736334","AY736332","AY736348","AY736341","AY736342","AY736338","AY736336","AY736343","AY736331","AY736344","AY736340","AY736333","AY736345","HQ676522","AF515260","EU221812","EU221813","EU221816","EU221817","EU221820","EU221821","EU221822","EU221824","EU221826","EU221827","EU221830","EU221834","EU221837","EU221838","EU221841","EU221842","EU221843","EU221845","EU221825","EU221855","EU221857","EU221858","EU221861","EU221866","EU221867","EU221868","EU221869","EU221870","KM106061","KM106062","KM106063","KF601953","JX103801","JX103803","JX103802","JN673862","JN673863","JN673864","JN673865","AF515244","JN673866","JN673867","JN673868","JN673869","JN673870","JN673872","JN673873","JN673874","JN673877","EU329109","JN673888","JN673889","JN673890","JN673891","JN673892","JN673893","JN673894","JN673895","JN673896","JN673901","KJ400019","JN673902","JN673903","EF540698","DQ514490","JX535956","EF540699","AM410355","AM410356","AY626843","AM410357","AM410358","AM410359","AM410360","DQ910512","DQ227298","DQ164504","AF425131","JN572308","JN572310","DQ514491","AY549841","AY549842","AY549843","AY549844","AF515251","KC254503","KC254466","KC254457","KC254480","KC254488","KC254451","KP318948","KC254467","KC254478","KC254501","KC254428","KC254471","KP318945","KP318939","KC254448","KC254442","KC254434","KC254476","KC254498","KC254497","KP318947","KC254472","KC254490","KC254502","KC254453","AF514838","KC254456","KC254482","KC254486","AF515257","AF515237","KC254473","KC254485","KC254439","KC254446","KC254464","KC254465","KC254487","KC254468","KC254474","KC254500","KP318938","KC254449","KC254432","KC254475","KC254455","KC254493","KC254459","KC254494","AF515233","KC254481","KC254463","KC254489","KP318943","EU329110","KC254429","AF515232","KP318942","KC254492","KC254441","AF515250","KC254491","KC254469","KC254433","KC254479","KC254450","KC254437","KC254477","KC254458","KP979014","KC254462","KC254452","KC254499","KC254435","KC900229","KC254460","KC254438","KC254470","KC254447","KC254461","KP318940","KP318941","KP318946","KC254454","KC254496","KC254445","KC254483","AF515245","KC254443","KP318944","EF588800","DQ432685","JN122020","JN122021","JN122022","JN122023","JN122024","AY529475","AY529476","EU571221","AY529478","EU571225","EU571224","EU571223","EU571222","AY529483","AF515240","AF515249","JX535957","JX535958","DQ514492","JX535959","JX535936","KJ196687","JN189126","AY268816","FR731967","FR731968","JX535917","JN189141","AY268803","AY268817","JN189086","JN189107","DQ514493","JN189087","FR731969","JN189108","AY268796","DQ514494","AY268778","FR731970","JN189109","JX535920","JN105314","JX535921","DQ514495","AY278398","JQ683004","JX535922","AY268808","JN189170","AY278399","AY268774","FR731974","AY278400","AY268813","JX535923","JX535924","DQ514478","HQ676526","DQ514496","JN189168","DQ514497","JN189088","AY268793","JN189103","AF515241","AY278403","JX535925","JX535926","JX535927","JX535928","JX535929","DQ514479","AY268784","JX535930","DQ514507","AY268791","JN189089","JN189117","JX535931","KJ196701","JQ683008","AY268810","JN189090","JX535932","JN189091","JN189119","JN189169","JX535933","JX535934","AY268789","JQ682994","JX535935","FR731986","AY268770","JN189098","JX535937","JX535938","AY268822","JX535939","JN189070","AY268807","FR731987","AY268814","FR731988","JN189120","AY268823","JN189140","KJ196700","AY268798","AY278404","AY268799","JN189171","FR731989","JN189093","JN189100","JX535941","AY268771","JX535942","JX535943","JX535944","JX535945","JN189094","JN189095","AY268762","JX535946","KC896601","DQ514498","JX535960","JX535947","AY268804","JX535948","JN189096","JX535950","KC878866","DQ514499","JN189145","DQ514500","JX535961","AY268824","AY278405","AY268765","KC896580","DQ514501","AF240671","EU797678","AY268772","AY268795","JN189167","JX535952","JX535953","AY736355","AY268761","JX028227","JX535955","AY536288","AY534840","AY536290","AY534841","KF212399","EF040611","AY534845","KJ528171","AY194076","KJ528172","AY534808","AY536294","AY194074","AY534817","AY534809","AY536355","AY536296","AY536297","KJ528173","AY194070","AY536298","KJ528175","AY534804","KJ528176","AY534822","AY534802","AY534842","AY534814","AY534820","AY536300","KJ528178","KJ528180","AY194078","AY536301","EF040613","AY534799","AY536303","AY534805","AY536304","KF212405","AY534827","AY536305","AY536306","AY194072","AY534811","KJ528182","EU907816","AY194068","AY536308","AY536292","AY534816","KF212406","KJ528183","AY534806","AY534803","KJ528187","KF212408","AY536309","EF040606","AY536311","AY536312","AY534839","AY534844","EU907820","AY536313","AY534836","KJ528189","AY534835","AY536314","AY536315","AY536316","AY534823","EU907834","AY536318","EU907836","AY536320","AY536321","EF040605","AY194077","AY534837","KJ528190","AY536291","AY536324","AY534801","AY534843","KJ528199","AY534807","AY534834","AY536327","AY536328","AY536329","AY536330","KF212411","KF212413","AY534832","AY536350","AY536331","AY536356","AY534838","AY536332","KJ528208","AY194069","KJ528211","EF040615","EF040604","AY534821","AY534824","AY536334","KF212414","AY534819","AY536335","AY534815","AY534825","KF212416","AY534800","AY534831","AY536338","KJ528230","AY536339","AY534812","AY536340","AY536341","EU907849","AY534810","AY534826","AY536342","AY536343","KF212420","AY536344","AY536345","AY536346","KJ528232","EF040607","AY536348","AY536349","EU907851","AY534833","AY536351","AY194071","AY536352","AY536353","AY534798","AY536354","AY194075","AY536359","AY534829","KJ528238","AY536360","AY194073","AY536361","AY536362","AY534813","EU907852","AY536363","AY534828","AY534818","AY536364","EU907857","AY536365","AY536366","KJ528245","EU907860","GU476634","GU476636","GU476637","GU476633","GQ428069","AY226124","AY226126","AY226121","AY226118","AY327837","AY226112","AY226114","AY226123","AY226122","AY226116","AY226120","AY226117","DQ914219","GU476715","GU476739","AF425132","JN572262","EF588802","JQ911718","DQ910515","AY651838","DQ910527","DQ164505","DQ642235","EU483026","EU483028","EU483029","AY083645","KT805027","KT805028","KT805029","KT805030","KT805031","AF425133","KT805032","KT805033","KT805034","KT805035","EF178649","AF469797","KM106065","GU476639","JF950910","EF178651","EF178655","EF178657","EF178659","GU476641","JF950911","EF178660","KM106067","KM106068","JQ911714","AF469786","KM106069","JF950912","HQ676528","AF515248","HQ676529","JQ700470","KJ196648","KC812970","JX040531","KC812959","KC812968","KC812960","JN869342","JF980703","KC812963","KC812972","KC812954","KC812967","JX040520","KC812955","JN869348","JX040532","KJ196699","KJ196642","KJ196676","KF591334","AY549830","KP851913","KP851917","AM410299","KC986872","KF113288","KF113290","KF591322","KC986875","KC986876","KF591336","AF448935","KF591339","AF425122","KF897955","KF897949","JN628839","JX103772","KJ464606","DQ514502","KJ464615","KJ464616","KJ464595","KJ196646","KJ464635","KJ464636","AY083631","AY083625","AY083626","AY083632","AY083627","AY083629","AY083628","AY083633","AY083634","EU483030","AY083624","AY083630","GU387213","GU387215","GU387216","GU387217","GU387219","GU387220","GU387221","GU387222","GU387224","GU387225","GU476649","GU387228","GU387229","GU387230","GU387233","GU387234","GU387243","GU387244","GU387246","GU387248","GU387251","GU387253","GU387255","GU387256","GU387258","GU387259","GU387264","GU387266","GU387267","EU483031","GU126728","GU126729","GU126726","EU483033","GU126725","GU126721","GU126724","GQ256241","GU126727","GQ256242","GU126723","GQ256173","GQ256174","GQ256214","GQ256166","GQ256176","GQ256177","GQ256178","GQ256179","GQ256180","GQ256197","GQ256182","GQ256235","GQ256187","GQ256189","GQ256190","GQ256167","GQ256191","GQ256192","GQ256193","GQ256194","GQ256195","GQ256230","GQ256199","GQ256200","GQ256201","HQ712019","GQ256203","GQ256204","GQ256205","GQ256206","GQ256172","GQ256207","GQ256209","GQ256168","HQ712018","GQ256210","GQ256211","GQ256212","GQ256213","HQ712017","GQ256169","GQ256215","GQ256216","GQ256217","HQ712015","HQ712016","GQ256220","GQ256221","GQ256223","GQ256170","GQ256202","GQ256224","GQ256226","GQ256227","GQ256228","GQ256229","GQ256231","GQ256234","GQ256236","GQ256237","GQ256238","GQ256240","EU483040","EU483041","JN572303","EF588804","EF588806","KF591330","EF588807","DQ514505","JN654975","JN654964","JN654973","KM106072","GU478854","GU478804","GU478865","GU478788","GU478801","GU478852","FJ360991","GU478806","GU478813","FJ360992","GU478866","FJ360994","FJ360993","GU478848","GU478809","GU478860","FJ360995","GU478850","GU478786","GU478834","GU478795","GU478859","GU478776","EU146057","GU478833","FJ360997","EU146056","GU478765","GU478868","GU478779","GU478853","FJ361004","FJ360998","GU478820","GU478818","GU478810","GU478766","FJ360999","GU478807","JQ736811","FJ361000","GU478781","FJ374265","KF652056","GU478772","GU478856","GU478822","GU478764","FJ361002","GU478803","GU478831","FJ361007","GU478819","GU478784","FJ361008","FJ361009","GU478837","GU478808","GU478815","GU478858","GU478843","GU478783","FJ361010","GU478812","FJ361011","GU478849","KF652057","FJ361012","GU478824","FJ361013","FJ361014","GU478816","FJ361015","GU478778","GU478851","FJ361016","GU478775","FJ361021","GU478767","GU478782","FJ361017","FJ361018","GU478768","GU478838","FJ361019","GU478771","GU478830","GU478825","GU478861","GU478805","GU478826","GU478847","GU478777","GU478832","GU478794","FJ361023","GU478828","FJ361024","GU478802","FJ361026","GU478770","GU478797","GU478862","FJ361027","GU478787","GU478827","GU478817","GU478785","FJ361029","FJ361030","GU478798","GU478839","FJ361031","GU478796","GU478835","KF652058","GU478800","GU478769","GU478845","GU478841","FJ361034","JN189131","GU376542","GU376545","GU376550","GU376551","GU376553","GU376555","GU376557","GU376559","DQ396555","DQ396557","DQ396558","DQ396559","DQ396560","DQ396561","DQ396562","DQ396566","DQ396569","DQ396571","DQ396572","DQ396573","DQ396575","DQ396577","AY540045","DQ396580","DQ396582","DQ396584","DQ396585","DQ396586","DQ396588","DQ396590","DQ396592","DQ396594","DQ396596","EU216748","DQ396598","DQ396600","GU478725","AM410361","DQ164506","DQ227299","DQ227303","DQ227300","DQ227301","DQ227302","AF515255","DQ845214","DQ845228","DQ845219","DQ845239","DQ845234","DQ845225","AY832906","DQ845221","DQ845230","DQ845240","DQ845218","DQ845222","DQ845227","DQ845224","HQ890406","HQ890407","JN572266","EU221872","EU221873","EU221875","DQ643359","HQ631334","DQ643361","HQ728343","DQ643362","DQ643363","FJ533858","HQ631286","DQ643364","HQ631344","HQ631321","DQ643366","HQ631357","HQ631326","DQ643367","DQ643368","FJ533860","DQ643369","FJ533863","HQ631356","HQ631294","HQ631351","HQ631296","DQ643374","DQ643375","HQ631269","DQ643378","DQ643379","HQ631359","DQ643380","HQ728345","HQ631332","HQ631349","HQ631297","DQ643382","EF588803","KC254425","KJ464641","KJ464642","KJ464643","KJ464647","KJ464648","KJ464644","KJ464651","GU387273","GU476662","GU387274","GU387276","GU387278","GU387279","GU476664","GU476666","GU476667","GU387281","GU476668","GU387283","KT805036","KT805037","KT805038","KT805039","KT805040","KT805041","KT805042","KT805043","KT805044","AF425136","JN572269","JN572270","JN572271","JN572272","HQ157338","GU376506","GU376548","GU376512","GU376519","GU376521","DQ642224","EF104517","DQ642225","EU292732","EF104518","DQ164507","DQ642228","DQ642230","DQ642231","JF514028","JF514032","EU483051","EU483053","EU483058","AY083637","EU483060","AY083636","DQ401124","DQ642246","EU483063","KF591329","DQ401125","DQ179642","EU483064","EU483066","DQ179643","DQ179645","EU483067","KC812964","JF514030","JF514022","JF514029","JF514035","JF514040","JF514043","JF514041","JF514034","JF514036","JF514031","JF514045","JF514038","JF514052","JF514046","JF514023","JF514055","JF514051","JF514033","GU476638","GU476707","GU476713","GU476719","GU476724","GU476725","GU476734","GU476735","GU387288","GU476699","DQ914220","EU831186","DQ914221","DQ914225","DQ914224","DQ914226","DQ914227","DQ914228","EU831188","DQ914229","EU831189","GU935615","DQ914223","DQ914232","DQ914233","EU831191","GQ256247","HQ597020","GQ256246","EU483069","HQ597019","GQ256243","AY083639","DQ642249","HQ157337","GU478757","GU478758","EU650061","EU250359","EF104519","JQ904113","KF591325","JQ904106","JQ904116","JQ904112","JQ904099","JQ904075","JQ904117","JQ904118","JQ904121","GU478740","GU478738","GU478739","KJ174512","GU478732","GU478731","GU478734","GU478742","GU478744","GU478746","GU478747","GU478737","GU478735","GU478743","GU478745","GU478741","KJ196690","KJ196689","DQ514508","DQ432687","DQ432688","KM106076","EF178650","KM106079","EF178661","KM106070","HQ676530","JN572273","KC155887","KC155899","KC155900","KC155885","KC155896","EF588810","FJ262717","EF588812","EF588813","FJ262718","AY651837","EF588818","EF588820","AY300045","DQ914203","DQ432680","DQ432683","DQ432684","DQ432681","DQ432682","HQ597016","KJ464603","KJ464609","KJ464610","KJ464612","DQ514503","KJ464613","KJ464619","KJ464622","KJ464624","KJ464628","KJ464630","KJ464632","KJ464638","KJ464639","JN572251","JN572254","AF159192","FJ825691","AF159193","DQ914174","DQ914176","EU831159","DQ914178","DQ914180","GU935600","KM435285","KM435286","GU935579","DQ914182","KM435287","DQ914186","EU831166","DQ914194","EU831170","JF950936","DQ432663","JN122025","GU935599","KM435289","DQ914181","GU935616","DQ914196","EU831174","DQ432661","EU831176","EU831178","KC254426","DQ514509","JX648120","DQ514510","DQ514513","EF540701","EF540702","DQ514514","HQ890412","HQ890413","HQ890417","FJ825690","DQ642258","JQ700472","JQ700473","JQ700474","JQ700475","JQ700476","JQ700480","JQ700481","JQ700486","JQ700488","JQ700490","JQ700491","JQ700492","JQ700493","JQ700495","JQ700496","JQ700498","JQ700503","JQ700499","JQ700500","JQ700506","HQ597021","EU483057","JX103810","EU269725","DQ643384","EU269729","EU269730","EU269731","DQ164509","DQ164510","DQ164511","DQ164512","DQ164513","DQ164514","DQ164515","DQ164516","DQ164517","DQ164518","DQ164519","DQ164520","DQ164523","DQ164524","DQ164525","DQ164526","DQ164527","GQ256249","GQ256250","KF709510","KJ196705","KJ196706","KF709512","KF709514","KF709516","AF159199","DQ642259","EU650067","DQ642260","EU650097","DQ642262","AF159200","EU650066","EU650088","EU650069","DQ642263","EU650062","EU650068","DQ642266","EU650063","EU650074","EU650082","EU650065","AF159196","EU650081","DQ642268","EU650073","DQ642270","EU650070","AF425140","AF425141","KJ464653","KJ464654","AF159182","KF685648","AF159183","KF685661","AF159189","KF685685","FJ825688","EU650091","FJ825687","FJ825686","KF685650","EU650089","EU650087","AF159178","AF159180","GU476671","AF159195","DQ642272","HQ676532","GU387231","EU650098","EU650090","FJ825683","KF685743","EU650095","GQ256251","EU650071","FJ825682","EU650079","EU650075","EU650080","EU650092","EU483027","AF159190","EU650076","EU650077","FJ825681","EU650094","FJ825679","AF159177","AF159197","EU650078","EU650093","FJ825678","KF685649","FJ825677","AY651840","JN189128","EF177286","HQ676534","KF020352","EF177271","KF020353","EF177287","JX476098","EF177277","KC878859","AY736335","EF177312","EF177311","JX476105","KF020354","JF713063","JF713056","EF177276","AY736352","EF177290","KC878861","KF020358","EF177291","EF177272","DQ514515","JX476109","JF827030","EF177307","KF020362","AY736349","KF020360","KC878869","EF177278","JX476111","KF020363","EF177279","JX476112","AY736337","JX476113","EF177313","GQ244336","EF177292","EF177273","EF177280","EF177293","DQ514489","KF020367","DQ202430","EF540703","AY736353","EF177294","EF177281","KF020368","AY736351","JF827028","EF177314","EF177282","EF177315","EF177275","AY534748","JX476116","KF020369","EF177284","JX476120","DQ514516","KF020372","EF177285","KF020374","EF177306","EF177295","GQ244335","EF540697","KF020376","KC896008","JX476119","KC878867","KC887498","KC878860","HQ676535","JX476123","KF020379","DQ514517","GQ244334","EF177309","KF020382","AY534749","EF177310","EF177302","EF177305","AY736350","EF177297","JN102164","KC878865","KC878868","AY736330","KF591328","JX476124","EF177304","DQ514519","EF177303","JN572279","JN572281","JN572283","JN572284","JN572285","JN572288","AF425142","JN572290","KM106082","EF178663","KM106084","KM106085","EF178664","KM106086","KC977426","JN572293","HQ890420","KT805047","KT805048","HQ890423","HQ890425","HQ890426","HQ890430","HQ890432","HQ890434","KF897951","KF897952","AY241586","AY300044","FJ784104","KJ196678","KF709517","KF709518","KF709520","AY545514","AY545509","AY545519","AY545510","AY545516","AY545507","AY545512","AY545511","AY545506","AY545515","AY545517","AY545518","AY545521","AY545513","HM559523","AY545523","DQ642250","DQ164528","DQ164529","DQ642251","JX103796","DQ642252","DQ164531","DQ642253","DQ164532","AY083646","DQ164533","JX103799","DQ642254","JX103798","DQ164534","DQ164530","DQ642255","DQ991141","DQ642256","DQ164535","JX103800","DQ642257","KM106087","EF178652","KM106066","EF178653","EF178656","KM106088","KM106089","DQ643385","AF514837","AY194067","KJ464657","DQ683431","JQ907390","EU269687","EU269688","EU269690","EU269692","AY138438","AY138436","AY138439","AY138442","KF700457","AY138437","KM106090","JF514049","KM106092","AY459178","AY459179","EU128518","AY459180","AY529484","AY459181","EU128519","EU128520","AY459182","DQ151957","DQ151964","EF551120","EF551123","EF551126","EF551127","DQ151960","DQ151983","EF551131","EF551132","EF551137","DQ151963","DQ151967","EF551138","DQ151966","DQ151968","EF551141","EF551142","EF551143","DQ151970","EF551146","EF551147","DQ151972","DQ151956","DQ151976","DQ151979","DQ151973","DQ151980","DQ151981","DQ151982","EF540704","DQ514522","AM410303","AM410342","AM410353","AM410334","AM410301","AM410311","AM410317","JF742607","AM410341","AM410312","AM410327","AM410313","AM410309","AM410333","AM410310","AM410307","AM410304","KT805049","KT805050","KT805051","KT805052","KT805053","KT805054","KT805055","KT805056","GU478736","GU478730","JN572304","JN572306","JN572307","HQ890435","JN572312","KT805059","KT805061","KT805062","KJ170856","GU387226","GU387227","GU476651","GU387239","GU387241","GU387249","GU387252","EF178662","HQ599520","GU387270","DQ910528","JX569713","DQ910532","JX569722","JX569730","KJ464658","KJ464659","KJ464660","DQ514523","KJ464661","DQ168817","DQ168821","GU478753","GU478755","GU478748","GU478750","GU478754","GU478751","GU478749","GU478756","GU478752","FJ360990","KF897954","KJ196656","KJ196683","KJ196631","KJ196628","KJ196696","KJ196663","DQ514524","KP271094","KF897957","KJ196671","KF897958","DQ514486","KF897960","KJ196660","KJ196651","KJ196667","KF897962","KF561674","KJ196695","KJ196669","KF897964","KF897965","KP271096","KJ196692","KJ196673","KJ196680","KF897970","KJ196709","KF561675","KJ196713","KF667627","KF897971","KP271097","KF897973","KJ196664","KF897974","KJ196698","KF897975","KP271098","KJ196707","KF561672","KJ196691","KJ196670","KF897977","KF897978","KF897979","KP271099","KJ196639","KJ196694","KF897981","KF897982","KJ196672","KF897983","KJ196710","KP271100","KJ170857","JQ907385","GU376566","GU376568","AF469798","GU476727","KT804997","HQ890418","KT804999","KT805057","KT805045","KT805001","KT805058","KT805002","AF425143","KT805003","KT805060","JN572253","KT805005","AF425138","KT805018","KT805008","HQ676538","KT805011","KT805012","KT805014","KT805016","KT805046","KM106093","KM106094","AY459183","HG422548","FJ384421","FJ384422","FJ384426","FJ384425","FJ384429","EF588822","EF588823","KM106095","KM106096","HQ597022","KF897985","KF897986","KF667630","KF667631","KF897989","KF897990","KF667632","KF667633","KF667635","KF667634","JN869354","JN869351","KP226784","KP226786","KP226787","KP226788","KP226791","KP226779","KP226782","KP226794","KP226795","KP226783","KP226796","KP226797","KP226801","KP226802","DQ683432","DQ683433","DQ683434","KM106097","KM106098","KM106099","GU476743","KM106101"]

x=filename

"""
a=[1,3,5]
b=[1,2,3]
set(a) - set(b)
set([5])
"""

diff_x=set(x)-set(testo)

#print(diff_x)
#print(len(diff_x))#5968


diff_y=set(testo)-set(x)

print(diff_y)
print(len(diff_y))#881
