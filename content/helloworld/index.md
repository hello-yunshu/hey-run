+++
title = "恭喜🎉，搭建成功啦！"
date = 2026-05-29T12:00:00+08:00
draft = false
description = ""
slug = "helloworld"
[build]
  list = false
  render = true
+++

<svg style="position:absolute;width:0;height:0">
  <defs>
    <filter id="liq">
      <feTurbulence id="liq-t" type="fractalNoise" baseFrequency="0.015" numOctaves="3" result="n" seed="2"/>
      <feDisplacementMap id="liq-d" in="SourceGraphic" in2="n" scale="0" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </defs>
</svg>

<style>
.cd-wrap{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:60vh;gap:1.5rem}
.cd-ring{position:relative;width:180px;height:180px}
.cd-ring svg.ring-svg{transform:rotate(-90deg);width:100%;height:100%}
.cd-ring circle{fill:none;stroke-width:6;stroke-linecap:round}
.cd-ring .bg{stroke:var(--neutral-200)}
.cd-ring .fg{stroke:var(--color-primary);stroke-dasharray:502;stroke-dashoffset:0;transition:stroke-dashoffset 1s linear}
.cd-num{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:4rem;font-weight:900;color:var(--color-primary);line-height:1;filter:url(#liq)}
.cd-hint{font-size:1rem;color:var(--neutral-400);letter-spacing:.02em}
.cd-hint span{font-weight:700;color:var(--color-primary)}
</style>

<div class="cd-wrap">
  <div class="cd-ring">
    <svg class="ring-svg" viewBox="0 0 180 180"><circle class="bg" cx="90" cy="90" r="80"/><circle class="fg" id="cd-fg" cx="90" cy="90" r="80"/></svg>
    <div class="cd-num" id="cd-num">5</div>
  </div>
  <p class="cd-hint">窗口将在 <span id="cd-sec">5</span> 秒后自动关闭</p>
</div>

<script>
(function(){
  var total=5,sec=5,circ=2*Math.PI*80;
  var fg=document.getElementById('cd-fg'),numEl=document.getElementById('cd-num'),sEl=document.getElementById('cd-sec');
  var disp=document.getElementById('liq-d'),turb=document.getElementById('liq-t');
  fg.style.strokeDasharray=circ;
  fg.style.strokeDashoffset='0';

  function animDisp(from,to,dur,cb){
    var t0=null;
    function frame(ts){
      if(!t0)t0=ts;
      var p=Math.min((ts-t0)/dur,1);
      var e=p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2;
      disp.setAttribute('scale',from+(to-from)*e);
      if(p<1)requestAnimationFrame(frame);
      else if(cb)cb();
    }
    requestAnimationFrame(frame);
  }

  function morph(n){
    animDisp(0,30,250,function(){
      numEl.textContent=n;
      turb.setAttribute('seed',Math.floor(Math.random()*100));
      animDisp(30,0,350);
    });
  }

  function tick(){
    sec--;
    morph(sec);
    if(sEl)sEl.textContent=sec;
    if(fg)fg.style.strokeDashoffset=circ*(1-sec/total);
    if(sec<=0){
      setTimeout(function(){
        window.close();
        document.querySelector('.cd-wrap').innerHTML='<p style="color:var(--neutral-400);font-size:1.1rem;padding:2rem 0">窗口已关闭，请手动关闭此标签页</p>';
      },700);
      return;
    }
    setTimeout(tick,1000);
  }
  setTimeout(tick,1000);
})();
</script>
