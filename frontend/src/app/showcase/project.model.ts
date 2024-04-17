/* eslint-disable prettier/prettier */
export interface Project {
  id: number | null;
  title: string;
  shorthand: string;
  thumbnail: string;
  short_description: string;
  text_body: string;
  author: string;
  onyen: string;
  public: boolean;
}

export interface ProjectResponse{
  id: number | null;
  title: string;
  shorthand: string;
  thumbnail: string;
  short_description: string;
  text_body: string;
  author: string;
  onyen: string;
  public: boolean;
}
