/* CareerCompass AI - Authentication */

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");
    const signupForm = document.getElementById("signupForm");
    const logoutButton = document.getElementById("logoutButton");

    async function showError(form, message) {
        let status = form.querySelector('[role="status"]');

        if (!status) {
            status = document.createElement("p");
            status.setAttribute("role", "status");
            form.appendChild(status);
        }

        status.textContent = message;
    }

    if (signupForm) {
        signupForm.addEventListener("submit", async event => {
            event.preventDefault();

            const fullName =
                signupForm.querySelector('[name="full_name"]')?.value.trim()
                || document.getElementById("full_name")?.value.trim()
                || document.getElementById("name")?.value.trim();

            const email = document.getElementById("email")?.value.trim();
            const password = document.getElementById("password")?.value;

            if (!fullName || !email || !password) {
                showError(signupForm, "Please fill in all required fields.");
                return;
            }

            try {
                const result = await API.post("/api/auth/register", {
                    full_name: fullName,
                    email,
                    password
                });

                if (result.access_token) {
                    localStorage.setItem("ccai_token", result.access_token);
                }

                if (result.user) {
                    localStorage.setItem("ccai_user", JSON.stringify(result.user));
                }

                window.location.href = result.access_token
                    ? "profile.html"
                    : "login.html";
            } catch (error) {
                showError(signupForm, error.message);
            }
        });
    }

    if (loginForm) {
        loginForm.addEventListener("submit", async event => {
            event.preventDefault();

            const email = document.getElementById("email")?.value.trim();
            const password = document.getElementById("password")?.value;

            if (!email || !password) {
                showError(loginForm, "Enter your email and password.");
                return;
            }

            try {
                const result = await API.post("/api/auth/login", {
                    email,
                    password
                });

                localStorage.setItem("ccai_token", result.access_token);

                if (result.user) {
                    localStorage.setItem("ccai_user", JSON.stringify(result.user));
                }

                window.location.href = "dashboard.html";
            } catch (error) {
                showError(loginForm, error.message);
            }
        });
    }

    if (logoutButton) {
        logoutButton.addEventListener("click", () => {
            localStorage.removeItem("ccai_token");
            localStorage.removeItem("ccai_user");
            window.location.href = "login.html";
        });
    }
});