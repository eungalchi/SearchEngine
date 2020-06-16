function enterkey() {
    if(window.event.keyCode == 13){ //키보드에 'Enter' 버튼 눌렀을 시
      search();
    }
  }

  $(document).on("click", ".enterBtn", function click(){
    search();
  });

  function search(){

    var text = $("#sch").val();

    $.ajax({
                url:'http://3.34.174.254:3000/python/py',//
                type : 'POST',
                data : {
                  text : text

                },
                success:function(data){
                  console.log(data);
                  var alertmessage = '';
                  for(var i = 0; i < data.length; i++){
                    alertmessage += ("Ira : " + data[i].ans.toString() + "입니다\n")
                    console.log((data[i].ans))
                  }
                  if(data == ''){
                    alert("DB에 데이터가 없습니다,,~_~")
                  }
                  else alert(alertmessage)
                  //alert(data[0].code)
                },
                error: function (request, status, error) {
                console.log('error!');
                alert("인식할 수 없는 키워드가 있습니다. 데이터 감사합니다 :)")
                //console.log(request.responseText);
                //alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
                },
                complete: function() {
                    console.log('검색 완료.');
                }
                

  });
  }

