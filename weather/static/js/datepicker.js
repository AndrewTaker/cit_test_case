jQuery.datetimepicker.setLocale('ru');
jQuery('#id_datetime').datetimepicker({
i18n:{
    ru:{
        months:[
            'Январь','Февраль','Март','Апрель',
            'Май','Июнь','Июль','Август',
            'Сентябрь','Октябрь','Ноябрь','Декабрь',
        ],
        dayOfWeek:[
            "Пн", "Вт", "Ср", "Чт",
            "Пт", "Сб", "Вс",
        ]
    }
},
format: 'Y-m-d',
timepicker: false,
dayOfWeekStart: 1,
constrainInput: true,
});
