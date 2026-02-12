export interface Todo {
  id: number;
  title: string;
  description?: string | null;
  is_completed: boolean;
  created_at?: string | null;
  updated_at?: string | null;
}

export interface TodoCreate {
  title: string;
  description?: string;
  is_completed: boolean;
}

export interface TodoUpdate {
  title?: string;
  description?: string;
  is_completed?: boolean;
}
