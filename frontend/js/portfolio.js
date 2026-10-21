/* CareerCompass AI - Study Planner */

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("taskForm");
    const taskInput = document.getElementById("task");
    const dateInput = document.getElementById("date");
    const list = document.getElementById("taskList");
    const progress = document.getElementById("progress");

    if (!form || !taskInput || !dateInput || !list) return;

    let tasks = JSON.parse(localStorage.getItem("ccai_tasks") || "[]");

    function saveTasks() {
        localStorage.setItem("ccai_tasks", JSON.stringify(tasks));
        renderTasks();
    }

    function renderTasks() {
        list.replaceChildren();

        let completed = 0;

        tasks.forEach((task, index) => {
            if (task.done) completed++;

            const item = document.createElement("li");

            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.checked = task.done;
            checkbox.setAttribute("aria-label", `Complete ${task.title}`);

            checkbox.addEventListener("change", () => {
                tasks[index].done = checkbox.checked;
                saveTasks();
            });

            const title = document.createElement("span");
            title.textContent =
                ` ${task.title} — Deadline: ${task.date}`;

            const removeButton = document.createElement("button");
            removeButton.type = "button";
            removeButton.textContent = "Delete";

            removeButton.addEventListener("click", () => {
                tasks.splice(index, 1);
                saveTasks();
            });

            item.append(checkbox, title, removeButton);
            list.appendChild(item);
        });

        if (progress) {
            progress.textContent = `Completed: ${completed} / ${tasks.length}`;
        }
    }

    form.addEventListener("submit", event => {
        event.preventDefault();

        const title = taskInput.value.trim();
        const date = dateInput.value;

        if (!title || !date) return;

        tasks.push({
            title,
            date,
            done: false
        });

        form.reset();
        saveTasks();
    });

    renderTasks();
});