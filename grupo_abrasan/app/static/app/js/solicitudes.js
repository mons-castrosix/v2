$(document).ready(function(){

    
  
    var dynamicVariable=$("#identificador").find("strong").text();
    $("#tabla").DataTable({
      "spaginationType": "simple_numbers_no_ellipses",
      "paging":false,
      
        dom:"Bfrtip",
        buttons:{
          dom:{
            button:{
              className:'btn'
            }
          },
          buttons:[
          {
            extend:"excel",
            text:'Exportar a excel',
            className:'btn btn-outlime-success',
            excelStyles:{
              template:'header_blue'
            },
            filename:"'Villa"+dynamicVariable+"'",
            title:"Explosión de Insumos Villa"+" "+dynamicVariable,
            sheetName:" "+dynamicVariable+""
            
          }]
        }
    });
   
    $(".dataTables_info ").hide()
    $(".buttons-excel ").hide()
   

  });
