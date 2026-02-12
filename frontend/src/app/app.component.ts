import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

import { TodoService } from './todo.service';
import { Todo } from './todo.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  todos: Todo[] = [];
  newTitle = '';
  newDescription = '';
  errorMessage = '';

  constructor(private todoService: TodoService) {}

  ngOnInit(): void {
    this.loadTodos();
  }

  loadTodos(): void {
    this.todoService.getTodos().subscribe({
      next: (todos) => {
        this.todos = todos;
      },
      error: () => {
        this.errorMessage = 'Unable to load todos.';
      },
    });
  }

  addTodo(): void {
    if (!this.newTitle.trim()) {
      return;
    }

    this.todoService
      .createTodo({
        title: this.newTitle.trim(),
        description: this.newDescription.trim() || undefined,
        is_completed: false,
      })
      .subscribe({
        next: (todo) => {
          this.todos = [todo, ...this.todos];
          this.newTitle = '';
          this.newDescription = '';
        },
        error: () => {
          this.errorMessage = 'Unable to create todo.';
        },
      });
  }

  toggleTodo(todo: Todo): void {
    this.todoService
      .updateTodo(todo.id, {
        is_completed: !todo.is_completed,
      })
      .subscribe({
        next: (updated) => {
          this.todos = this.todos.map((item) =>
            item.id === updated.id ? updated : item,
          );
        },
        error: () => {
          this.errorMessage = 'Unable to update todo.';
        },
      });
  }

  deleteTodo(todo: Todo): void {
    this.todoService.deleteTodo(todo.id).subscribe({
      next: () => {
        this.todos = this.todos.filter((item) => item.id !== todo.id);
      },
      error: () => {
        this.errorMessage = 'Unable to delete todo.';
      },
    });
  }
}
