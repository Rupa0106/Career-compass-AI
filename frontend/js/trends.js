/* CareerCompass AI - Skill Explorer */

document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("skillSearch");
    const categorySelect = document.getElementById("skillCategory");
    const cards = [...document.querySelectorAll("[data-skill-card]")];
    const emptyMessage = document.getElementById("noSkillsFound");

    function filterSkills() {
        const search = (searchInput?.value || "").trim().toLowerCase();
        const category = categorySelect?.value || "all";
        let visibleCount = 0;

        cards.forEach(card => {
            const text = card.textContent.toLowerCase();
            const cardCategory = card.dataset.category || "all";

            const matchesSearch = text.includes(search);
            const matchesCategory =
                category === "all" || cardCategory === category;

            const visible = matchesSearch && matchesCategory;
            card.hidden = !visible;

            if (visible) visibleCount++;
        });

        if (emptyMessage) {
            emptyMessage.hidden = visibleCount !== 0;
        }
    }

    searchInput?.addEventListener("input", filterSkills);
    categorySelect?.addEventListener("change", filterSkills);

    filterSkills();
});