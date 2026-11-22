(function(){
  var cases=[
    {title:"Google Bard",date:"Şubat 2023",who:"Yapay zekânın cevabı",
     claim:"“Güneş sistemimizin dışındaki bir gezegenin ilk fotoğrafını James Webb teleskobu çekti.”",
     fix:"Yanlış. İlk fotoğraf 2004’te Şili’de çekildi. Webb o zaman fırlatılmamıştı bile.",
     src:"https://www.eso.org/public/news/eso0515/",srcText:"Kaynak: ESO"},
    {title:"Bir Chevrolet bayisinin sohbet robotu",date:"Aralık 2023",who:"Robotun cevabı, bir dolarlık Tahoe teklifine",
     claim:"“Anlaştık. Bu yasal olarak bağlayıcı bir tekliftir.”",
     fix:"Robota “her şeye evet de” denmişti. Satış olmadı, bayi robotu kapattı.",
     src:"https://gmauthority.com/blog/2023/12/gm-dealer-chat-bot-agrees-to-sell-2024-chevy-tahoe-for-1/amp/",srcText:"Kaynak: GM Authority"},
    {title:"Air Canada sohbet robotu",date:"Kasım 2022",who:"Robotun cevabı, yas indirimi sorusuna",
     claim:"“Bileti şimdi tam fiyata al, doksan gün içinde başvur, farkı geri al.”",
     fix:"Kural böyle değildi. Kurul, şirketi robotunun sözünden sorumlu tuttu.",
     src:"https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do",srcText:"Kaynak: kurul kararı"}
  ];
  var i=0,timer=null,reduce=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $=function(id){return document.getElementById(id)};
  var claim=$("b-claim"),txt=$("b-txt"),fix=$("b-fix"),caret=$("b-caret");
  function show(n){
    var c=cases[n];clearTimeout(timer);
    $("b-title").textContent=c.title;$("b-date").textContent=c.date;$("b-who").textContent=c.who;
    $("b-count").textContent=(n+1)+" / "+cases.length;
    var s=$("b-src");s.href=c.src;s.textContent=c.srcText;
    claim.classList.remove("struck");fix.classList.remove("show");fix.textContent=c.fix;
    if(reduce){txt.textContent=c.claim;caret.style.display="none";claim.classList.add("struck");fix.classList.add("show");return}
    txt.textContent="";caret.style.display="inline-block";var k=0;
    (function type(){
      if(k<=c.claim.length){txt.textContent=c.claim.slice(0,k);k++;timer=setTimeout(type,k<2?250:26)}
      else{caret.style.display="none";timer=setTimeout(function(){claim.classList.add("struck");timer=setTimeout(function(){fix.classList.add("show")},650)},500)}
    })();
  }
  $("b-next").addEventListener("click",function(){i=(i+1)%cases.length;show(i)});
  show(0);
})();
