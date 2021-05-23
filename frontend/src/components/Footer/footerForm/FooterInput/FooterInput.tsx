import React from 'react'
import TextField from '@material-ui/core/TextField'
import {withStyles} from '@material-ui/core/styles'
import styles from './FooterInput.module.scss'

const CssTextField = withStyles({
  root: {
    '& label.Mui-focused': {
      color: 'rgba(0, 0, 0, 0.54)',
    },
    '& .MuiInput-underline:after': {
      borderBottomColor: 'rgba(176, 151, 106, 1)',
    },
    '& .MuiOutlinedInput-root': {
      borderRadius: '0',
      '& fieldset': {
        borderColor: 'rgba(176, 151, 106, 1)',
        borderWidth: '2px',
      },
      '&:hover fieldset': {
        borderColor: 'rgba(145, 125, 87, 1)',
      },
      '&.Mui-focused fieldset': {
        borderColor: 'rgba(176, 151, 106, 1)',
      },
    },
  },
})(TextField)

interface IFooterInput {
  id: string,
  label: string
}

export const FooterInput: React.FC<IFooterInput> = (props) => {
  const {id, label} = props

  return (
    <div className={styles.formInputAndLabel}>
      <CssTextField
        className={styles.input}
        id={id}
        label={label}
        variant="outlined"
        required
      />
    </div>
  )
}