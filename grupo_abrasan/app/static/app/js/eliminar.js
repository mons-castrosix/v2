
function eliminarProducto(id){
    Swal.fire({
        "title":"¿Estás seguro de eliminar este registro?",
        "text": "Esta acción no se puede deshacer.",
        "icon": "question",
        "showCancelButton":true,
        "cancelButtonText":"No, Cancelar.",
        "confirmButtonText":"Si, Eliminar.",
        "reverseButtons":true,
        "confirmButtonColor":"#F20505",
        "cancelButtonColor":"#110273"
    }) 
    .then(function (result){
        if (result.isConfirmed){
            window.location.href="/inventario/eliminar-producto/"+id+"/"
        }
    })
}
function eliminarVilla(id){
    Swal.fire({
        "title":"¿Estás seguro de eliminar este registro?",
        "text": "Esta acción no se puede deshacer.",
        "icon": "question",
        "showCancelButton":true,
        "cancelButtonText":"No, Cancelar.",
        "confirmButtonText":"Si, Eliminar.",
        "reverseButtons":true,
        "confirmButtonColor":"#F20505",
        "cancelButtonColor":"#110273"
    }) 
    .then(function (result){
        if (result.isConfirmed){
            window.location.href="/inventario/eliminar-villa/"+id+"/"
        }
    })
}
function eliminarObra(id){
    Swal.fire({
        "title":"¿Estás seguro de eliminar este registro?",
        "text": "Esta acción no se puede deshacer.",
        "icon": "question",
        "showCancelButton":true,
        "cancelButtonText":"No, Cancelar.",
        "confirmButtonText":"Si, Eliminar.",
        "reverseButtons":true,
        "confirmButtonColor":"#F20505",
        "cancelButtonColor":"#110273"
    }) 
    .then(function (result){
        if (result.isConfirmed){
            window.location.href="/inventario/eliminar-obra/"+id+"/"
        }
    })
}
function eliminarBodega(id){
    Swal.fire({
        "title":"¿Estás seguro de eliminar este registro?",
        "text": "Esta acción no se puede deshacer.",
        "icon": "question",
        "showCancelButton":true,
        "cancelButtonText":"No, Cancelar.",
        "confirmButtonText":"Si, Eliminar.",
        "reverseButtons":true,
        "confirmButtonColor":"#F20505",
        "cancelButtonColor":"#110273"
    }) 
    .then(function (result){
        if (result.isConfirmed){
            window.location.href="/inventario/eliminar-bodega/"+id+"/"
        }
    })
}
function eliminarProductoBodega(bodega,id){
    
    Swal.fire({
        "title":"¿Estás seguro de eliminar este registro?",
        "text": "Esta acción no se puede deshacer.",
        "icon": "question",
        "showCancelButton":true,
        "cancelButtonText":"No, Cancelar.",
        "confirmButtonText":"Si, Eliminar.",
        "reverseButtons":true,
        "confirmButtonColor":"#F20505",
        "cancelButtonColor":"#110273"
    }) 
    .then(function (result){
        if (result.isConfirmed){
            window.location.href="/inventario/eliminar-producto-bodega/"+bodega+"/"+id+"/"
        }
    })
}