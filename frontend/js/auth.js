/* CareerCompass AI - Authentication */

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");
    const signupForm = document.getElementById("signupForm");
    const logoutButton = document.getElementById("logoutButton");

    function showMessage(form, message) {
        if (!form) return;

        let status = form.querySelector('[role="status"]');

        if (!status) {
            status = document.createElement("p");
            status.setAttribute("role", "status");
            status.style.marginTop = "12px";
            status.style.fontSize = "14px";
            form.appendChild(status);
        }

        status.textContent = message;
        status.style.display = "block";
    }

    // LOGIN
    if (loginForm) {
        loginForm.addEventListener("submit", async (event) => {
            event.preventDefault();

            const email = document.getElementById("email")?.value.trim();
            const password = document.getElementById("password")?.value;

            if (!email || !password) {
                showMessage(loginForm, "Please enter your email and password.");
                return;
            }

            const button = loginForm.querySelector(
                'button[type="submit"]'
            );

            const originalText = button?.textContent;

            if (button) {
                button.disabled = true;
                button.textContent = "Signing in...";
            }

            try {
                if (!window.API) {
                    throw new Error(
                        "API script did not load. Please check js/api.js."
                    );
                }

                const result = await window.API.post("/api/auth/login", {
                    email: email,
                    password: password
                });

                if (!result.access_token) {
                    throw new Error(
                        "Login response did not contain an access token."
                    );
                }

                localStorage.setItem("ccai_token", result.access_token);

                if (result.user) {
                    localStorage.setItem(
                        "ccai_user",
                        JSON.stringify(result.user)
                    );
                }

                showMessage(loginForm, "Login successful! Opening dashboard...");

                window.location.href = "dashboard.html";

            } catch (error) {
                console.error("Login error:", error);

                showMessage(
                    loginForm,
                    error.message || "Login failed. Please try again."
                );

            } finally {
                if (button) {
                    button.disabled = false;
                    button.textContent = originalText || "Sign In";
                }
            }
        });
    }

    // SIGNUP
    if (signupForm) {
        signupForm.addEventListener("submit", async (event) => {
            event.preventDefault();

            const fullName =
                signupForm.querySelector('[name="full_name"]')?.value.trim()
                || document.getElementById("full_name")?.value.trim()
                || document.getElementById("name")?.value.trim();

            const email = document.getElementById("email")?.value.trim();
            const password = document.getElementById("password")?.value;

            if (!fullName || !email || !password) {
                showMessage(signupForm, "Please fill in all required fields.");
                return;
            }

            try {
                const result = await window.API.post("/api/auth/register", {
                    full_name: fullName,
                    email: email,
                    password: password
                });

                if (result.access_token) {
                    localStorage.setItem("ccai_token", result.access_token);
                }

                if (result.user) {
                    localStorage.setItem(
                        "ccai_user",
                        JSON.stringify(result.user)
                    );
                }

                window.location.href = result.access_token
                    ? "profile.html"
                    : "login.html";

            } catch (error) {
                console.error("Signup error:", error);
                showMessage(signupForm, error.message);
            }
        });
    }

    // LOGOUT
    if (logoutButton) {
        logoutButton.addEventListener("click", () => {
            localStorage.removeItem("ccai_token");
            localStorage.removeItem("ccai_user");

            window.location.href = "login.html";
        });
    }
});
