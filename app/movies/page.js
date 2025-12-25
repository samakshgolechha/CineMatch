import { Suspense } from 'react';
import MoviesClientPage from './MoviesClientPage';

export default function Page({ searchParams }) {
  return (
    <Suspense fallback={<div className="text-white">Loading...</div>}>
      <MoviesClientPage searchParams={searchParams} />
    </Suspense>
  );
}
