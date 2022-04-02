import Link from "next/link";

import classess from './MainNavigation.module.css'

function MainNavigation() {
  return (
    <header className={classess.header}>
      <div className={classess.logo}>Fuzzy Durian</div>
      <nav  className={classess.nav}>
        <ul>
          <li><Link href='/'>Cek Data</Link></li>
          <li><Link href='/dataset'>Dataset</Link></li>
          <li><Link href='/penulis'>Penulis</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;
