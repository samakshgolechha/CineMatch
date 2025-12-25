import { Suspense } from "react";
import MoviesClientPage from "./MoviesClientPage";

export default function MoviesPage() {
  return (
    <Suspense fallback={<div className="text-white p-10">Loading movies...</div>}>
      <MoviesClientPage />
    </Suspense>
  );
}
