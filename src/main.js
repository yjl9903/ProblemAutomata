marked.setOptions({
    renderer: new marked.Renderer(),
    gfm: true,
    tables: true,
    breaks: false,
    pedantic: false,
    sanitize: false,
    smartLists: true,
    smartypants: false,
    highlight: function(code) {
        return hljs.highlightAuto(code).value;
    }
});
window.MathJax.Hub.Config({
    showProcessingMessages: false, //关闭js加载过程信息
    messageStyle: "none", //不显示信息
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
        inlineMath: [["$", "$"], ["\\(", "\\)"]], //行内公式选择符
        displayMath: [["$$", "$$"], ["\\[", "\\]"]], //段内公式选择符
        skipTags: ["script", "noscript", "style", "textarea", "pre", "code", "a"] //避开某些标签
    },
    "HTML-CSS": {
        availableFonts: ["STIX", "TeX"], //可选字体
        showMathMenu: false //关闭右击菜单显示
    }
});


var ws = new WebSocket("ws://localhost:3001/");
ws.isopen = false;

ws.onopen = function(){
    ws.isopen = true;
    vtitle.title = "Connected";
    // app.message = "Connected!";
    // ws.send("Hello!");
    ws.ts = window.setInterval(function(){
        // console.log("abc");
        ws.send(JSON.stringify({
            "type": "request",
            "value": true
        }));
    }, 3000);
};

ws.onmessage = function(msg){
    data = JSON.parse(msg.data);
    if (data.type == "cpp"){
        vm.content = "<pre><code class=\"cpp\">" 
                    + hljs.highlightAuto(data.content).value 
                    + "</code></pre>";
        // console.log(data.content);
    }
};

ws.onclose = function(){
    ws.isopen = false;
    vtitle.title = "Disconnected";
    window.clearInterval(ws.ts);
}

window.MathJax.Hub.Queue(["Typeset", MathJax.Hub, document.getElementById('md')]);
