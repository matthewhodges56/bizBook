document.getElementById("btnLogin").addEventListener("click", async function(){
    let userEmail = document.getElementById("email").value;
    let userPassword = document.getElementById("password").value;
    //const regEmail = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/g

    let strMessage = "";
    let blnError = false;

    // if (!regEmail.test(email)) {
    //     blnError = true;
    //     strMessage += "<p>Invalid Email.</p>"
    // }

    if (userEmail.length < 4) {
        blnError = true;
        strMessage += "<p>No email provided</p>"
    }

    if (userPassword.length < 1) {
        blnError = true;
        strMessage += "<p>No password provided</p>"
    }

    if (blnError) {
        Swal.fire({
            title: "ERROR",
            html: strMessage,
            icon: "error",
            iconColor: "black",
            color: "black",
            confirmButtonColor: "black"
        });
    } else {
        // Swal.fire({
        //     title: "SUCCESS",
        //     html: `Logging in...`,
        //     icon: "SUCCESS",
        //     iconColor: "black",
        //     color: "black",
        //     showConfirmButton: false,
        //     timer: 2000,
        //     allowOutsideClick: false,
        //     allowEscapeKey: false
        // });

        try {
            const response = await fetch('/check_user', {  // Replace with your actual login route
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email: userEmail, password: userPassword }),
            });
    
            if (response.ok) {
                // Login successful, handle redirect or response
                const data = await response.json();
                if (data.success) {
                    // Redirect to a protected page or update the UI
                    window.location.href = '/';  // Example redirect
                } else {
                    // error
                }
            } else {
                // Login failed, display error message
                console.error('Login failed:', response.status);
            }
        } catch (error) {
            console.error('Error during login:', error);
        }
    }
})