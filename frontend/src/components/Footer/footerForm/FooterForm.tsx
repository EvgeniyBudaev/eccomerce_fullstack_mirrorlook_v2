import React from 'react'
import styles from './FooterForm.module.scss'
import FooterInput from './FooterInput'

export const FooterForm: React.FC = () => {
  return (
    <div className={styles.form}>
      <div className={styles.formTitle}>
        Заполните форму и менеджер свяжется с Вами
      </div>
      <form noValidate autoComplete="off">
        <FooterInput id="footerInput1" label="Ваше имя" />
        <FooterInput id="footerInput2" label="Ваше телефон" />
        <button className={styles.button} type={'submit'}>
          <svg
            width="10"
            height="18"
            viewBox="0 0 10 18"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M0 16.3909L1.51671 18L10 9L1.51671 0L0 1.60909L6.96658 9L0 16.3909Z"
              fill="white"
              fillOpacity="0.8"
            />
          </svg>
        </button>
      </form>
    </div>
  )
}