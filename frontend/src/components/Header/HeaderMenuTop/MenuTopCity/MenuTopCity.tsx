import React from 'react'
import cn from 'classnames'
import styles from './MenuTopCity.module.scss'

export const MenuTopCity: React.FC = () => {
  return (
    <span className={cn(styles.menuTopCity)}>
      <svg
        width="25"
        height="25"
        viewBox="0 0 25 25"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g opacity="0.6">
          <rect width="25" height="25" fill="white" />
          <path
            className={styles.icon0}
            d="M12.4999 11.9791C11.0614 11.9791 9.89575 10.8135 9.89575 9.37498C9.89575 7.93644 11.0614 6.77081 12.4999 6.77081C13.9385 6.77081 15.1041 7.93644 15.1041 9.37498C15.1041 10.8135 13.9385 11.9791 12.4999 11.9791Z"
          />
          <path
            className={styles.icon0}
            d="M12.5 2.09375C8.48328 2.09375 5.21558 5.36146 5.21558 9.37813C5.21558 14.0479 11.4322 21.6354 11.6968 21.9552L12.5 22.9292L13.3031 21.9552C13.5677 21.6344 19.7843 14.0479 19.7843 9.37813C19.7843 5.36042 16.5166 2.09375 12.5 2.09375ZM12.5 19.6115C10.5437 17.0458 7.29891 12.2 7.29891 9.37813C7.29891 6.51042 9.63224 4.17708 12.5 4.17708C15.3677 4.17708 17.701 6.51042 17.701 9.37813C17.701 12.1958 14.4562 17.0438 12.5 19.6115Z"
          />
        </g>
      </svg>
      <span>Москва</span>
    </span>
  )
}