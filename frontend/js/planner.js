```javascript
/* CareerCompass AI - Study Planner */

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("taskForm");
    const taskInput = document.getElementById("task");
    const dateInput = document.getElementById("date");
    const list = document.getElementById("taskList");
    const progress = document.getElementById("progress");

    if (!form || !taskInput || !dateInput || !list) return;

    let tasks = [];

    function showMessage(message) {
        let status = document.getElementById("taskStatus");

        if (!status) {
            status = document.createElement("p");
            status.id = "taskStatus";
            status.setAttribute("role", "status");
            form.insertAdjacentElement("afterend", status);
        }

        status.textContent = message;
    }

    function renderTasks() {
        list.replaceChildren();

        let completed = 0;

        tasks.forEach(task => {
            if (task.is_completed) completed++;

            const item = document.createElement("li");

            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.checked = task.is_completed;
            checkbox.setAttribute("aria-label", `Complete ${task.title}`);

            checkbox.addEventListener("change", async () => {
                checkbox.disabled = true;

                try {
                    const updated = await API.request(`/api/tasks/${task.id}`, {
                        method: "PATCH",
                        body: JSON.stringify({
                            is_completed: checkbox.checked
                        })
                    });

                    task.is_completed = updated.is_completed;
                    showMessage("Task status updated.");
                    renderTasks();
                } catch (error) {
                    checkbox.checked = task.is_completed;
                    checkbox.disabled = false;
                    showMessage(`Could not update task: ${error.message}`);
                }
            });

            const title = document.createElement("span");
            title.textContent =
                ` ${task.title} — Deadline: ${task.due_date || "Not set"}`;

            const removeButton = document.createElement("button");
            removeButton.type = "button";
            removeButton.textContent = "Delete";

            removeButton.addEventListener("click", async () => {
                removeButton.disabled = true;

                try {
                    await API.request(`/api/tasks/${task.id}`, {
                        method: "DELETE"
                    });

                    tasks = tasks.filter(item => item.id !== task.id);
                    showMessage("Task deleted.");
                    renderTasks();
                } catch (error) {
                    removeButton.disabled = false;
                    showMessage(`Could not delete task: ${error.message}`);
                }
            });

            item.append(checkbox, title, removeButton);
            list.appendChild(item);
        });

        if (progress) {
            progress.textContent = `Completed: ${completed} / ${tasks.length}`;
        }
    }

    async function loadTasks() {
        try {
            tasks = await API.get("/api/tasks/");
            renderTasks();
            showMessage("Tasks loaded from your account.");
        } catch (error) {
            showMessage(`Could not load tasks: ${error.message}`);
        }
    }

    form.addEventListener("submit", async event => {
        event.preventDefault();

        const title = taskInput.value.trim();
        const date = dateInput.value;

        if (!title) {
            showMessage("Please enter a task title.");
            return;
        }

        const submitButton = form.querySelector('[type="submit"]');

        if (submitButton) submitButton.disabled = true;

        try {
            const created = await API.post("/api/tasks/", {
                title,
                description: "",
                due_date: date || null
            });

            tasks.unshift(created);
            form.reset();
            renderTasks();
            showMessage("Task saved to the database.");
        } catch (error) {
            showMessage(`Could not save task: ${error.message}`);
        } finally {
            if (submitButton) submitButton.disabled = false;
        }
    });

    loadTasks();
});
```
