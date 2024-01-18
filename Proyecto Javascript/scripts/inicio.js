let d_C = 0;
        window.onpageshow = function () {
            const but_close = document.getElementById("button_close_entry");
            const logo_white = document.getElementById("logo_white");
            rotate_animation = setInterval(frame, 10)
            function frame () {
                if (d_C == 360) {
                    clearInterval(rotate_animation);
                    but_close.style.visibility = "visible";

                } else {
                    d_C += 10
                    logo_white.style.rotate = d_C + "deg"
                }
            }  
        }
        
        function close_entry() {
            const entry_div = document.getElementById("entry_image")
            const button_pickup = document.getElementById("b_pickup")
            const button_delivery = document.getElementById("b_delivery")
            const wpp_div = document.getElementsByClassName("wpp")[0]
            entry_div.style.display = "none"
            button_pickup.style.visibility = "visible"
            button_delivery.style.visibility = "visible"
            wpp_div.style.visibility = "visible"
            
        }