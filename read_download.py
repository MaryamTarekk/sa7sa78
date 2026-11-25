
(function(){
var $=function(s){return document.querySelectorAll(s)},g=function(i){return document.getElementById(i)},rd=matchMedia("(prefers-reduced-motion:reduce)").matches;
var hd=g("hd");function sc(){hd.classList.toggle("sc",scrollY>20)}addEventListener("scroll",sc,{passive:true});sc();
g("mb").onclick=function(){hd.classList.toggle("op")};$("#lk a").forEach(function(a){a.onclick=function(){hd.classList.remove("op")}});
/* ecosystem */
var M=["إدارة المبيعات","نقطة البيع POS","إدارة المخزون","إدارة المشتريات","إدارة العملاء","إدارة الموردين","الحسابات والخزينة","المحاسبة","الفروع والمخازن","الموارد البشرية","CRM","التقارير والتحليلات","المستخدمين والصلاحيات"],eco=g("eco"),sv=g("sv"),L=[];
M.forEach(function(t,i){var a=i/M.length*Math.PI*2-Math.PI/2,x=50-41*Math.cos(a+Math.PI)*-1,y=50+40*Math.sin(a);x=50+41*Math.cos(a);
var n=document.createElement("div");n.className="nd";n.textContent=t;n.style.left=(100-x)+"%";n.style.top=y+"%";eco.appendChild(n);
var l=document.createElementNS("http://www.w3.org/2000/svg","line");l.setAttribute("x1",50);l.setAttribute("y1",50);l.setAttribute("x2",100-x);l.setAttribute("y2",y);sv.appendChild(l);
n.onmouseenter=function(){l.classList.add("h");n.classList.add("h")};n.onmouseleave=function(){l.classList.remove("h");n.classList.remove("h")}});
/* features */
var F=[["المبيعات","إدارة المبيعات","من عرض السعر لحد الفاتورة والتحصيل في دورة واحدة.",["فواتير بيع إلكترونية متوافقة مع الفاتورة الإلكترونية","عروض أسعار تتحول لأوامر بيع بنقرة","حجز الكميات من المخزن","حسابات العملاء وتاريخ المشتريات","تسجيل السداد نقدًا أو عبر البنك"]],
["نقطة البيع","نقطة بيع سريعة","شاشة بيع بتعمل باللمس تخلّص الطابور بسرعة.",["بيع سريع بالباركود","طرق دفع متعددة","فواتير فورية","تتبع مبيعات كل كاشير"]],
["المخزون","مخزون تحت السيطرة","اعرف بضاعتك فين وإمتى تحتاج تطلب.",["دعم عدة مخازن ومستودع مركزي","جرد بالباركود","تنبيه عند حد إعادة الطلب","تحويلات بين الفروع","أرقام التشغيلات وتواريخ الصلاحية"]],
["المالية","حسابات منظمة","قيود يومية آلية وتقارير مالية جاهزة.",["شجرة حسابات متعددة المستويات","مراكز تكلفة","قيود يومية آلية","حركات الخزائن والبنوك","أرباح وخسائر وميزان مراجعة"]],
["العملاء والموردين","علاقات واضحة","ملف موحد لكل عميل ومورد.",["ملف عميل متكامل بكل المعاملات","حدود ائتمان ومتابعة الاستحقاق","كشوف حساب للطباعة والإرسال","أوامر شراء ومتابعة الاستلام","جداول سداد الموردين"]],
["فريق العمل","فريق بصلاحيات محكمة","كل موظف يشوف ويعمل اللي يخصه بس.",["أدوار وصلاحيات مخصصة","سجل مراقبة للتعديلات","ملفات الموظفين","مسيرات الرواتب والإجازات"]],
["الفروع","فروع متصلة","تحكم في كل فروعك من شاشة واحدة.",["عدة فروع ومستودعات في شاشة واحدة","تحويلات بتأكيد استلام إلكتروني","ربحية كل فرع"]],
["التقارير","تقارير تفهمها","رؤية واضحة تساعدك تقرر.",["أرباح وخسائر","الأكثر مبيعًا","أداء الفروع","كشوف الحساب"]]];
var tb=g("tabs"),pn=g("pnl");
function show(i){$("#tabs button").forEach(function(b,k){b.classList.toggle("on",k==i)});var d=F[i];
pn.innerHTML='<div><h3>'+d[1]+'</h3><p>'+d[2]+'</p></div><div class="mock"><div class="wh"><i></i><i></i><i></i><span>'+d[0]+'</span></div><div class="wb">'+d[3].map(function(f){return'<div class="tr">'+f+'<span class="tg on"></span></div>'}).join("")+'</div></div>';
pn.classList.remove("sw");void pn.offsetWidth;if(!rd)pn.classList.add("sw")}
F.forEach(function(d,i){var b=document.createElement("button");b.textContent=d[0];b.onclick=function(){show(i)};tb.appendChild(b)});show(0);
/* flows */
var FL=[["المبيعات","المخزون","المالية","المحاسبة","التقارير"],["المشتريات","الموردين","المخزون","المدفوعات"],["العملاء","المبيعات","التحصيل","حسابات العملاء"],["الموظفين","الصلاحيات","العمليات","الأداء"]];
g("fl").innerHTML=FL.map(function(r){return'<div class="fr">'+r.map(function(t){return'<b>'+t+'</b>'}).join('<span class="ar"></span>')+'</div>'}).join("");
/* sectors */
var S=[["◧","متاجر التجزئة","بيع سريع بالباركود وجرد دوري وتنبيه قبل نفاد الأصناف."],["▦","السوبر ماركت","شاشة بيع باللمس لطوابير أقل وتتبع مبيعات كل كاشير."],["▤","الجملة","أوامر بيع وحسابات عملاء وحدود ائتمان ومتابعة التحصيل."],["▣","شركات التوزيع","مخازن متعددة وتحويلات بين الفروع وكشوف حساب للعملاء."],["◉","المطاعم والكافيهات","نقطة بيع سريعة وطرق دفع متعددة ومتابعة المخزون."],["◈","الشركات التجارية","مشتريات وموردين وحسابات ومحاسبة وتقارير أرباح وخسائر."],["⬡","الأنشطة متعددة الفروع","كل الفروع في شاشة واحدة وصلاحيات لكل فرع."]],sc2=g("sc");
S.forEach(function(d,i){var b=document.createElement("button");b.className="sx"+(i?"":" on");b.innerHTML="<span>"+d[0]+"</span><h3>"+d[1]+"</h3><p>"+d[2]+"</p>";b.onclick=function(){$(".sx").forEach(function(x){x.classList.remove("on")});b.classList.add("on")};sc2.appendChild(b)});
/* reveal */
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{threshold:.12});
$("section h2,section .sb,.eb,.eco,.sh,.fr,.sc2,.wy div,.sl div,.band").forEach(function(el){el.classList.add("rv");el.style.setProperty("--d",(Array.prototype.indexOf.call(el.parentNode.children,el)*.07)+"s");io.observe(el)});
})();
