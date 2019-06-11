<?php
// include settings for secret key
include 'settings.php';
?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>    
    <style>
        body {
            font-family:sans;
            background-color:black;
            color:white;
            padding: 20px;
        }
        
        button {
            font-size: 160px;
        }
        
        h1 {
            font-size: 200px
            padding: 0;
            margin:0;
            display: flex;
            align-items:center;
        }
        
        h2 {
            font-size: 100px;
        }
                
        .switch {
          position: relative;
          display: inline-block;
          width: 260px;
          height: 134px;
        }

        .switch input { 
          opacity: 0;
          width: 0;
          height: 0;
        }

        .slider {
          position: absolute;
          cursor: pointer;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background-color: #ccc;
          -webkit-transition: .4s;
          transition: .4s;
        }

        .slider:before {
          position: absolute;
          content: "";
          height: 126px;
          width: 126px;
          left: 4px;
          bottom: 4px;
          background-color: white;
          -webkit-transition: .4s;
          transition: .4s;
        }

        input:checked + .slider {
          background-color: #fcaf3e;
        }

        input:focus + .slider {
          box-shadow: 0 0 1px #fcaf3e;
        }

        input:checked + .slider:before {
          -webkit-transform: translateX(126px);
          -ms-transform: translateX(126px);
          transform: translateX(126px);
        }
    </style>
    <script>
        $(document).ready(function(){
        
            // on and off switch clicks
            $('.check-box').click(function() {   
               if ($(this).data('value') == '1') {
                unset($(this).data('flag'));
                $(this).data('value', '0');
               } else {
                set($(this).data('flag'));
                $(this).data('value', '1');
               }
            });
            
            // on page load prepopulate checkboxes
            $('.check-box').each(function() {
                var thisCheckBox = $(this);
                $.ajax({
                    url: "/flag/" + thisCheckBox.data('flag'),
                    data: {},
                    success: function (data) {
                        thisCheckBox.data('value', data.message);
                        if (data.message == '1') thisCheckBox.prop( "checked", true );
                    },
                });
            });
        });

        function set(flag) {
            $.ajax({
                url: "/flag/"+flag+"/set",
                headers: {"api-key": "<?=md5($secretAPIKey)?>"}
            });
        }

        function unset(flag) {
            $.ajax({
                url: "/flag/"+flag+"/unset",
                headers: {"api-key": "<?=md5($secretAPIKey)?>"}
            });
        }
    </script>
</head>
    <body>
        <h1><img src="img/gnome-system-monitor.png"/> &nbsp; WiFi Outlets</h1>
        <?php
            foreach ($outletsEnabled as $outletName => $flags){
            ?>
            <h2><?=$outletName?></h2>
            <?php
                foreach ($flags as $flag){
                ?>
                <label class="switch">
                  <input class="check-box" data-flag="<?=$flag?>" data-value="1" type="checkbox">
                  <span class="slider"></span>
                </label>
                <br/><br/><br/><br/>
            <?php
                }
            }
        ?>
    </body>
</html>
