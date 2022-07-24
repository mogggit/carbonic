var jsonWordLevels = {'w1':'初級', 'w2':'中級', 'w3':'中高'};
var jsonTypeNames = {'fill_in_the_blank':'填空題', 'multiple_choice':'選擇題'};
var jsonWordLevelClasses = {'w1':'texti-w1', 'w2':'texti-w2', 'w3':'texti-w3'};

function alertError(argMsg) {
    if(argMsg==0) {
        toastr.error('伺服器沒有回應');
    }
    else if(argMsg==500) {
        toastr.error('內部伺服器錯誤');
    }
    else {
        toastr.error(argMsg);
    }
}

function castBool2Bin(argVal) {
    return argVal == true ? 1 : 0;
}

String.prototype.replaceAll = function(argFind, argRep){
    return this.replace(new RegExp(argFind, 'gm'),argRep);
}