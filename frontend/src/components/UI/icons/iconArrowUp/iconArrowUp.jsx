import React from 'react'
import styles from './iconArrowUp.module.scss'
import cn from 'classnames'

const IconArrowUp = (props) => {
  const {rotate} = props
 const iconArrowUp = cn(styles.iconArrowUp, {[styles.rotate]: rotate})

  return (
    <svg
      width="16"
      height="8"
      viewBox="0 0 16 8"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={iconArrowUp}
    >
      <path
        opacity="0.8"
        d="M1.4303 0L0 1.21337L8 8L16 1.21337L14.5697 0L8 5.57326L1.4303 0Z"
        fill="black"
        fillOpacity="0.8"
      />
    </svg>
  )
}

export default IconArrowUp
