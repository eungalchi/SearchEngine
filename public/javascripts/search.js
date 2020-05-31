function enterkey() {
    if(window.event.keyCode == 13){
      search();
    }
  }

  $(document).on("click", ".enterBtn", function click(){
    search();
  });

  function search(){

    var text = $("#sch").val();

    $.ajax({
                url:'http://3.34.174.254:3000/python/py',//3.34.174.254:3000
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
                    alert("키워드를 중심으로 다시 검색해 주십시오.")
                  }
                  else alert(alertmessage)
                  //alert(data[0].code)
                },
                error: function (request, status, error) {
                console.log('error!');
                alert("예제를 더 만들겠습니다,,,, 데이터 감사합니다 :)")
                //console.log(request.responseText);
                //alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
                },
                complete: function() {
                    console.log('검색 완료.');
                }
                

  });
  }

