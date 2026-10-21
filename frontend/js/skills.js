/* CareerCompass AI - Roadmap */

document.addEventListener("DOMContentLoaded", () => {
    const generateButton = document.getElementById("generateRoadmap");
    const goalInput = document.getElementById("careerGoal");
    const skillsInput = document.getElementById("currentSkills");
    const hoursInput = document.getElementById("studyHours");
    const result = document.getElementById("roadmapResult");

    if (!generateButton || !goalInput || !result) return;

    generateButton.addEventListener("click", async () => {
        const careerGoal = goalInput.value.trim();

        if (!careerGoal) {
            result.textContent = "Enter your career goal first.";
            return;
        }

        const payload = {
            career_goal: careerGoal,
            current_skills: (skillsInput?.value || "")
                .split(",").map(skill => skill.trim()).filter(Boolean),
            study_hours_per_week: Number(hoursInput?.value || 10)
        };

        result.textContent = "Generating your roadmap...";

        try {
            const data = await API.post("/api/roadmaps/generate", payload);

            result.replaceChildren();

            const title = document.createElement("h2");
            title.textContent = data.title || "Your Learning Roadmap";
            result.appendChild(title);

            const description = document.createElement("p");
            description.textContent = `Career goal: ${data.career_goal || careerGoal}`;
            result.appendChild(description);

            const stages = data.stages || {};

            Object.entries(stages).forEach(([stage, content]) => {
                const section = document.createElement("section");
                const heading = document.createElement("h3");
                heading.textContent = stage;
                section.appendChild(heading);

                const paragraph = document.createElement("p");
                paragraph.textContent =
                    typeof content === "string"
                        ? content
                        : JSON.stringify(content, null, 2);

                section.appendChild(paragraph);
                result.appendChild(section);
            });
        } catch (error) {
            result.textContent =
                "Roadmap could not be generated. Check backend status and API route.";
            console.error("Roadmap error:", error.message);
        }
    });
});