import React from 'react'
import classNames from 'classnames'
import {Link} from 'react-router-dom'
import styles from './Footer.module.scss'
import FooterLogoAndSocial from './FooterLogoAndSocial'
import FooterForm from './footerForm'
import FooterPolitics from './FooterPolitics'
import {ROUTES} from '../../routes'

export const Footer: React.FC = () => {
  const footerLogoAndSocial = classNames(
    styles.innerItem,
    styles.footerLogoAndSocial
  )
  const footerContacts = classNames(styles.innerItem, styles.footerContacts)

  return (
    <footer className={styles.footer}>
      <div className={styles.container}>
        <div className={styles.inner}>
          <div className={styles.innerItem}>
            <h4>Каталог</h4>
            <ul>
              <li>
                <Link to={ROUTES.HOME}>Венецианские зеркала</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Напольные зеркала</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Зеркала в рамах</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Зеркальные панно</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Зеркало-солнце</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Консоли</Link>
              </li>
            </ul>
          </div>
          <div className={styles.innerItem}>
            <h4>Информация</h4>
            <ul>
              <li>
                <Link to={ROUTES.HOME}>О магазине</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Каталог</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Распродажа</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Доставка и оплата</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Контакты</Link>
              </li>
            </ul>
          </div>
          <div className={styles.innerItem}>
            <h4>Подборки</h4>
            <ul>
              <li>
                <Link to={ROUTES.HOME}>Скидки</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Лидеры продаж</Link>
              </li>
              <li>
                <Link to={ROUTES.HOME}>Новинки</Link>
              </li>
            </ul>
          </div>
          <div className={footerContacts}>
            <h4>Контакты</h4>
            <ul>
              <li>
                <a href="tel:89261113968">+7 (926) 111-39-68</a>
              </li>
              <li>
                <a href="mailto:mirror-look@mail.ru">mirror-look@mail.ru</a>
              </li>
              <li>
                <p>г. Москва, ул. Рябиновая, 43 корпус 2</p>
              </li>
            </ul>
          </div>
          <div className={footerLogoAndSocial}>
            <FooterLogoAndSocial />
          </div>
        </div>
        <FooterForm />
        <FooterPolitics />
      </div>
    </footer>
  )
}