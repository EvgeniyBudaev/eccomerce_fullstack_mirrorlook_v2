import React from 'react'
import {NavLink} from 'react-router-dom'
import styles from './HeaderMenuBottom.module.scss'
import {ROUTES} from '../../../routes'

export const HeaderMenuBottom = () => {
    const activeLink = {
    fontSize: '18px',
    lineHeight: 1.25,
    fontFamily: 'Montserrat',
    fontWeight: 500,
    pointerEvents: 'none',
    cursor: 'default',
  }

  return (
    <div className={styles.headerMenuBottom}>
      <nav>
        <ul>
          <li>
            <NavLink to={ROUTES.HOME} exact activeStyle={activeLink}>
              Главная
            </NavLink>
          </li>
          <li>
            <NavLink to={ROUTES.ABOUT} activeStyle={activeLink}>
              О магазине
            </NavLink>
          </li>
        </ul>
      </nav>
    </div>
  )
}