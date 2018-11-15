var ws = new WebSocket("ws://localhost:3001/");

ws.onopen = function(){
    app.message = "Connected!";
    ws.send("Hello!");
};

ws.onmessage = function(msg){
    // app.message = msg.data;
    // console.log(msg)
    app.res = msg.data;
};

var app = new Vue({
    el: "#msgbox",
    data: {
        send: 'Hello Vue',
        res: ''
    },
    methods: {
        sendMsg: function(){
            ws.send(this.send);
        }
    }
});