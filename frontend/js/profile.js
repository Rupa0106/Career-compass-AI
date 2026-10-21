/* CareerCompass AI - Student Profile */

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("profileForm");
    const message = document.getElementById("message");

    if (!form) return;

    const fields = [
        "branch",
        "year",
        "skills",
        "interests",
        "goal",
        "hours"
    ];

    function showMessage(text) {
        if (message) message.textContent = text;
    }

    async function loadProfile() {
        const token = localStorage.getItem("ccai_token");
        if (!token) return;

        try {
            const profile = await API.get("/api/profiles/me");

            if (profile.branch) document.getElementById("branch").value = profile.branch;
            if (profile.study_year) document.getElementById("year").value = profile.study_year;

            document.getElementById("skills").value =
                (profile.current_skills || []).join(", ");

            document.getElementById("interests").value =
                (profile.interests || []).join(", ");

            if (profile.career_goal) {
                document.getElementById("goal").value = profile.career_goal;
            }

            if (profile.weekly_study_hours !== undefined) {
                document.getElementById("hours").value =
                    profile.weekly_study_hours;
            }
        } catch (error) {
            console.info("Profile not loaded:", error.message);
        }
    }

    form.addEventListener("submit", async event => {
        event.preventDefault();

        const payload = {
            branch: document.getElementById("branch").value,
            study_year: Number(document.getElementById("year").value),
            current_skills: document.getElementById("skills").value
                .split(",").map(value => value.trim()).filter(Boolean),
            interests: document.getElementById("interests").value
                .split(",").map(value => value.trim()).filter(Boolean),
            career_goal: document.getElementById("goal").value,
            weekly_study_hours: Number(document.getElementById("hours").value)
        };

        if (!localStorage.getItem("ccai_token")) {
            localStorage.setItem("ccai_profile_draft", JSON.stringify(payload));
            showMessage("Profile draft saved in this browser. Login after backend setup to save it to your account.");
            return;
        }

        try {
            await API.put("/api/profiles/me", payload);
            showMessage("Profile saved successfully.");
        } catch (error) {
            showMessage("Could not save profile: " + error.message);
        }
    });

    loadProfile();
});