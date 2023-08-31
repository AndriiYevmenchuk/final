$(document).ready(function(){
    $(".ajaxLoader").hide();
    $(".custom-control-input").on('click',function(){
        var _filterObj={};
        $(".custom-control-input").each(function(index,ele){
            var _filterVal=$(this).val();
			var _filterKey=$(this).data('filter');
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
        });
        $.ajax({
            url:'/catalog/filter-data',
            data:_filterObj,
            data_type:'json',
            beforeSend:function(){
                $(".ajaxLoader").show();
            },
            success:function(res){
                console.log(res);
                $("#filteredProducts").html(res.data);
                $(".ajaxLoader").hide();
            }
        });
    });
});